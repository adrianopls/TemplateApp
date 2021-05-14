
import wx

from classes import class_register
from . import interface

from classes.UIManager import UIManager


class MyApp(wx.App):
    
    # def __init__(self):
    #     #
    #     _redirect =  False
    #     _filename = None
    #     _useBestVisual = False
    #     _clearSigInt = True
    #     #
    #     super().__init__(_redirect, _filename, 
    #                                    _useBestVisual, _clearSigInt
    #     ) 
        
    def OnInit(self):
        self._mwc = None
        class_register.register_app_classes()   
        self.load_app_interface()  
        return True           
 
    def load_app_interface(self):
        # Load app Interface
        self._mwc = interface.load()
        # 
        if self._mwc:
            # View-Controller app will bypass this call to self._mwc.view
            self._mwc.Show()    
            #
            self.SetTopWindow(self._mwc.view)      
            
    def get_main_window_controller(self):
        return self._mwc
              
    #TODO: REMOVER ISSO!!    
    def get_manager_class(self, obj_tid):
        return UIManager    

    