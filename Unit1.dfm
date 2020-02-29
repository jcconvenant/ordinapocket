object Form1: TForm1
  Left = 218
  Top = 110
  BorderIcons = [biSystemMenu, biMinimize]
  BorderStyle = bsSingle
  Caption = 'Ordinapocket'
  ClientHeight = 348
  ClientWidth = 415
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  Icon.Data = {
    0000010001002020100000000000E80200001600000028000000200000004000
    0000010004000000000080020000000000000000000010000000000000000000
    0000000080000080000000808000800000008000800080800000C0C0C0008080
    80000000FF0000FF000000FFFF00FF000000FF00FF00FFFF0000FFFFFF000000
    0000000000000000000000000000000000000000000000000000000000000000
    0000000000000000000000000000000888888888888888888888888880000000
    0000000000000000000000000000000888888888888888888888888880000008
    8888888888888888888888888000000877878787878787878787878780000000
    8878787878787878787878780000000087878787878787878787878800000000
    8778787878787878787878780000000008888888888888888888888000000000
    0008000000000000000080000000000000888888888888888888880000000000
    0088888888888888888888800000000008888888888888888888888000000000
    088000000000000000000880000000000880A000000000000000088000000000
    088000000000000000000880000000000880AAAAAA0000000000088000000000
    088000000000000000000880000000000880AA0A000000000000088000000000
    088000000000000000000880000000000880AAAAAA0000000000088000000000
    088000000000000000000880000000000880AA0AA00000000000088000000000
    0880000000000000000008800000000008800000000000000000088000000000
    0088888888888888888888000000000000000000000000000000000000000000
    000000000000000000000000000000000000000000000000000000000000FFFF
    FFFFFFFFFFFFC0000003C0000003C0000003C0000003C0000003C0000003E000
    0007E0000007E0000007F000000FF000000FFC00003FF000000FF000000FF000
    000FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF000
    000FF000000FF000000FF000000FF000000FF000000FFFFFFFFFFFFFFFFF}
  OldCreateOrder = False
  Position = poScreenCenter
  OnCreate = FormCreate
  OnDestroy = FormDestroy
  PixelsPerInch = 96
  TextHeight = 13
  object GroupBox1: TGroupBox
    Left = 0
    Top = 0
    Width = 153
    Height = 329
    Align = alLeft
    Caption = 'Program'
    TabOrder = 0
    object Panel1: TPanel
      Left = 2
      Top = 199
      Width = 149
      Height = 128
      Align = alBottom
      BevelOuter = bvNone
      TabOrder = 0
      object Button1: TButton
        Left = 8
        Top = 5
        Width = 129
        Height = 21
        Caption = 'Load'
        TabOrder = 0
        OnClick = Button1Click
      end
      object Button2: TButton
        Left = 8
        Top = 58
        Width = 129
        Height = 21
        Caption = 'Run'
        TabOrder = 1
        OnClick = Button2Click
      end
      object Button3: TButton
        Left = 8
        Top = 104
        Width = 129
        Height = 21
        Caption = 'Stop'
        TabOrder = 2
        OnClick = Button3Click
      end
      object Button5: TButton
        Left = 8
        Top = 28
        Width = 129
        Height = 21
        Caption = 'Store'
        TabOrder = 3
        OnClick = Button5Click
      end
      object Button6: TButton
        Left = 8
        Top = 81
        Width = 129
        Height = 21
        Caption = 'Reset'
        ParentShowHint = False
        ShowHint = True
        TabOrder = 4
        OnClick = Button6Click
      end
    end
    object StringGrid1: TStringGrid
      Left = 2
      Top = 15
      Width = 149
      Height = 184
      Align = alClient
      ColCount = 2
      DefaultColWidth = 63
      DefaultRowHeight = 17
      RowCount = 101
      Options = [goFixedVertLine, goFixedHorzLine, goVertLine, goHorzLine, goRangeSelect, goEditing]
      ScrollBars = ssVertical
      TabOrder = 1
      OnDrawCell = StringGrid1DrawCell
      ColWidths = (
        63
        63)
      RowHeights = (
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17
        17)
    end
  end
  object StatusBar1: TStatusBar
    Left = 0
    Top = 329
    Width = 415
    Height = 19
    Panels = <>
    SimplePanel = True
    ExplicitWidth = 413
  end
  object GroupBox2: TGroupBox
    Left = 288
    Top = 0
    Width = 125
    Height = 185
    Caption = 'Output'
    TabOrder = 2
    object Memo1: TMemo
      Left = 2
      Top = 15
      Width = 121
      Height = 168
      Align = alClient
      ReadOnly = True
      TabOrder = 0
    end
  end
  object GroupBox4: TGroupBox
    Left = 156
    Top = 186
    Width = 257
    Height = 143
    Caption = 'Processor'
    TabOrder = 3
    object Label1: TLabel
      Left = 8
      Top = 18
      Width = 46
      Height = 13
      Caption = 'CO (init) : '
    end
    object Label2: TLabel
      Left = 8
      Top = 40
      Width = 17
      Height = 13
      Caption = 'RI :'
    end
    object Label3: TLabel
      Left = 8
      Top = 56
      Width = 21
      Height = 13
      Caption = 'CO :'
    end
    object Label5: TLabel
      Left = 136
      Top = 40
      Width = 29
      Height = 13
      Caption = 'TMP :'
    end
    object Label6: TLabel
      Left = 136
      Top = 56
      Width = 27
      Height = 13
      Caption = 'ACC :'
    end
    object SpinEdit1: TSpinEdit
      Left = 59
      Top = 14
      Width = 41
      Height = 22
      EditorEnabled = False
      MaxLength = 2
      MaxValue = 99
      MinValue = 0
      TabOrder = 0
      Value = 0
    end
    object CheckBox1: TCheckBox
      Left = 8
      Top = 117
      Width = 98
      Height = 17
      Caption = 'Step-by-step'
      ParentShowHint = False
      ShowHint = True
      TabOrder = 1
    end
    object Button4: TButton
      Left = 176
      Top = 113
      Width = 75
      Height = 25
      Caption = 'Continue'
      ParentShowHint = False
      ShowHint = False
      TabOrder = 2
      OnClick = Button4Click
    end
    object Button7: TButton
      Left = 8
      Top = 80
      Width = 241
      Height = 25
      Caption = 'Instructions'
      ParentShowHint = False
      ShowHint = True
      TabOrder = 3
    end
  end
  object GroupBox3: TGroupBox
    Left = 156
    Top = 0
    Width = 129
    Height = 186
    Caption = 'Input'
    TabOrder = 4
    object Button8: TButton
      Left = 48
      Top = 152
      Width = 73
      Height = 25
      Caption = 'Enter'
      TabOrder = 0
      OnClick = Button8Click
    end
    object Button9: TButton
      Left = 8
      Top = 56
      Width = 33
      Height = 25
      Caption = '1'
      TabOrder = 1
      OnClick = Button9Click
    end
    object Button10: TButton
      Left = 48
      Top = 56
      Width = 33
      Height = 25
      Caption = '2'
      TabOrder = 2
      OnClick = Button9Click
    end
    object Button11: TButton
      Left = 88
      Top = 56
      Width = 33
      Height = 25
      Caption = '3'
      TabOrder = 3
      OnClick = Button9Click
    end
    object Button12: TButton
      Left = 8
      Top = 88
      Width = 33
      Height = 25
      Caption = '4'
      TabOrder = 4
      OnClick = Button9Click
    end
    object Button13: TButton
      Left = 48
      Top = 88
      Width = 33
      Height = 25
      Caption = '5'
      TabOrder = 5
      OnClick = Button9Click
    end
    object Button14: TButton
      Left = 88
      Top = 88
      Width = 33
      Height = 25
      Caption = '6'
      TabOrder = 6
      OnClick = Button9Click
    end
    object Button15: TButton
      Left = 8
      Top = 120
      Width = 33
      Height = 25
      Caption = '7'
      TabOrder = 7
      OnClick = Button9Click
    end
    object Button16: TButton
      Left = 48
      Top = 120
      Width = 33
      Height = 25
      Caption = '8'
      TabOrder = 8
      OnClick = Button9Click
    end
    object Button17: TButton
      Left = 88
      Top = 120
      Width = 33
      Height = 25
      Caption = '9'
      TabOrder = 9
      OnClick = Button9Click
    end
    object Button18: TButton
      Left = 8
      Top = 152
      Width = 33
      Height = 25
      Caption = '0'
      TabOrder = 10
      OnClick = Button9Click
    end
    object Edit1: TEdit
      Left = 8
      Top = 24
      Width = 113
      Height = 21
      AutoSize = False
      MaxLength = 3
      TabOrder = 11
      OnKeyPress = Edit1KeyPress
    end
  end
  object OpenDialog1: TOpenDialog
    Left = 368
    Top = 24
  end
  object SaveDialog1: TSaveDialog
    Filter = 'Tous les fichiers|*.*'
    Title = 'Sauvegarder votre programme ...'
    Left = 304
    Top = 25
  end
end
