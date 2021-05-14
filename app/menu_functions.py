# -*- coding: utf-8 -*-
"""
Created on Thu May 13 16:48:07 2021

@author: Adriano
"""

import os
import wx

from . import interface
from classes.UIManager import UIManager


def on_open(*args, **kwargs):
    wildcard = "Load segmentated file (*.png)|*.png"
    try:
        fdlg = wx.FileDialog(wx.App.Get().GetTopWindow(), 
                             "Choose file", 
                             wildcard=wildcard, 
                             style=wx.FD_OPEN|wx.FD_FILE_MUST_EXIST
        )
        if fdlg.ShowModal() == wx.ID_OK:
            file_name = fdlg.GetFilename()
            dir_name = fdlg.GetDirectory()
            fdlg.Destroy()
        else:
            fdlg.Destroy()
            return
        fullfilename = os.path.join(dir_name, file_name)    
        
        print (fullfilename)
        
        #gripy_app = wx.App.Get()
        #gripy_app.load_project_data(fullfilename)
    except Exception as e:
        print ('ERROR [on_open]:', str(e))
        raise



def on_open_model(*args, **kwargs):
    UIM = UIManager()      
    mwc = interface.get_main_window_controller()
    UIM.create('crossplot_controller', mwc.uid)