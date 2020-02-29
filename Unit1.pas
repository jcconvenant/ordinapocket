unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Grids, ExtCtrls, ComCtrls, Spin;

type
  TForm1 = class(TForm)
    GroupBox1: TGroupBox;
    StatusBar1: TStatusBar;
    Panel1: TPanel;
    Button1: TButton;
    Button2: TButton;
    Button3: TButton;
    StringGrid1: TStringGrid;
    GroupBox2: TGroupBox;
    Memo1: TMemo;
    OpenDialog1: TOpenDialog;
    GroupBox4: TGroupBox;
    Label1: TLabel;
    SpinEdit1: TSpinEdit;
    CheckBox1: TCheckBox;
    Button4: TButton;
    Label2: TLabel;
    Label3: TLabel;
    Label5: TLabel;
    Label6: TLabel;
    Button5: TButton;
    SaveDialog1: TSaveDialog;
    Button6: TButton;
    Button7: TButton;
    GroupBox3: TGroupBox;
    Button8: TButton;
    Button9: TButton;
    Button10: TButton;
    Button11: TButton;
    Button12: TButton;
    Button13: TButton;
    Button14: TButton;
    Button15: TButton;
    Button16: TButton;
    Button17: TButton;
    Button18: TButton;
    Edit1: TEdit;
    procedure FormCreate(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
    procedure Button5Click(Sender: TObject);
    procedure FormDestroy(Sender: TObject);
    procedure Button6Click(Sender: TObject);
    procedure Edit1KeyPress(Sender: TObject; var Key: Char);
    procedure Button9Click(Sender: TObject);
    procedure Button8Click(Sender: TObject);
    procedure StringGrid1DrawCell(Sender: TObject; ACol, ARow: Integer;
      Rect: TRect; State: TGridDrawState);
  private
    { Déclarations privées }
  public
    Annuler, Run, pasinc, continue, DemandeEntree: boolean;
    RI, Entree: string;
    CO: shortint;
    cache: TStringlist;
    TMP, ACC: SmallInt;
    procedure ResetAll;
    procedure Charger(fichier: string);
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}

procedure TForm1.Charger(fichier: string);
var
  t: TStringlist;
  i: Integer;
  ok: boolean;
begin
  ResetAll;
  t := TStringlist.Create;
  t.LoadFromFile(fichier);
  if t.Count > 100 then
  begin
    ShowMessage('Error : program too long (' + IntToStr(t.Count) + ' words)');
    t.Free;
    Exit;
  end;
  if t.Text = '' then
  begin
    ShowMessage('Error : empty file');
    t.Free;
    Exit;
  end;
  ok := true;
  for i := 0 to t.Count - 1 do
    if Length(t[i]) > 3 then
      ok := false;
  if ok then
  begin
    for i := 0 to t.Count - 1 do
      StringGrid1.Rows[i + 1][1] := t[i];
    cache.Assign(t);
  end
  else
    ShowMessage('Error : program line too long');
  t.Free;
end;

procedure TForm1.ResetAll;
var
  i: Integer;
begin
  Label2.Caption := 'RI :';
  Label3.Caption := 'CO :';
  Label5.Caption := 'TMP :';
  Label6.Caption := 'ACC :';
  Memo1.Clear;
  Edit1.Text := '';
  RI := '0';
  CO := SpinEdit1.Value - 1;
  TMP := 0;
  ACC := 0;
  for i := 1 to 100 do
    StringGrid1.Rows[i][1] := '';
end;

procedure TForm1.FormCreate(Sender: TObject);
var
  i: Integer;
begin
  Entree := '';
  Application.HintPause := 0;
  Application.HintHidePause := 50000;
  Application.HintColor := clBtnFace;
  StringGrid1.Rows[0][0] := 'Adresse';
  StringGrid1.Rows[0][1] := 'Données';
  for i := 1 to 10 do
    StringGrid1.Rows[i][0] := '0' + IntToStr(i - 1);
  for i := 11 to 100 do
    StringGrid1.Rows[i][0] := IntToStr(i - 1);
  Button7.Hint := '0  INP Input' + #13#10 + '1  OUT Output' + #13#10 +
    '2  CLA Clear And Add' + #13#10 + '3  STO Store' + #13#10 + '4  ADD Add' +
    #13#10 + '5  SUB Sub' + #13#10 + '6  SHL Shift Left' + #13#10 +
    '7  SHR Shift Right' + #13#10 + '8  TMP Temporary' + #13#10 + '9  JMP Jump'
    + #13#10 + 'A  TAC Test And Content' + #13#10 + 'B  LTH Lesser Than' +
    #13#10 + 'C  GTH Greater Than' + #13#10 + 'F  Halt And Reset';
  CheckBox1.Hint := 'Step-by-step mode executes the' + #13 + #10 +
    'program line by line';
  cache := TStringlist.Create;
  ResetAll;
  Run := false;
  Annuler := false;
end;

procedure TForm1.Button1Click(Sender: TObject);
begin
  OpenDialog1.InitialDir := ExtractFileDir(Application.ExeName);
  if not Run then
    if OpenDialog1.Execute then
      Charger(OpenDialog1.FileName);
end;

procedure TForm1.Button2Click(Sender: TObject);
var
  Rect: TGridRect;
  InfoAdr: string;
begin
  CO := SpinEdit1.Value - 1;
  TMP := 0;
  ACC := 0;

  Run := true;
  DemandeEntree := false;
  Annuler := false;
  pasinc := false;
  while not Annuler do
  begin
    if pasinc then
      pasinc := false
    else
      Inc(CO);
    while CO > 99 do
      CO := CO - 100;

    Rect.Left := 1;
    Rect.Top := CO + 1;
    Rect.Right := 1;
    Rect.Bottom := CO + 1;
    StringGrid1.Selection := Rect;

    RI := StringGrid1.Rows[1 + CO][1];

    if RI = '' then
    begin
      ShowMessage('No data at ' + IntToStr(CO));
      Annuler := true;
    end
    else
    begin

      InfoAdr := StringGrid1.Rows[1 + StrToInt(RI[2] + RI[3])][1];

      if RI[1] = '0' then
      begin
        DemandeEntree := true;
        StatusBar1.SimpleText := 'Please enter a value ...';
        while DemandeEntree do
          Application.ProcessMessages;
        StatusBar1.SimpleText := '';
        StringGrid1.Rows[1 + StrToInt(RI[2] + RI[3])][1] := Entree;
      end;
      if RI[1] = '1' then
        if InfoAdr <> '' then
          Memo1.Lines.Add(IntToStr(StrToInt(InfoAdr)))
        else
          ShowMessage('No data at ' + IntToStr(CO));
      if RI[1] = '2' then
        if InfoAdr <> '' then
          ACC := StrToInt(InfoAdr)
        else
          ShowMessage('No data at ' + IntToStr(CO));
      if RI[1] = '3' then
        StringGrid1.Rows[1 + StrToInt(RI[2] + RI[3])][1] := IntToStr(ACC);
      if RI[1] = '4' then
      begin
        if InfoAdr <> '' then
        begin
          ACC := ACC + StrToInt(InfoAdr);
          while ACC > 999 do
            ACC := ACC - 1000;
        end
        else
          ShowMessage('No data at ' + IntToStr(CO));
      end;
      if RI[1] = '5' then
      begin
        if InfoAdr <> '' then
        begin
          ACC := ACC - StrToInt(InfoAdr);
          while ACC < 0 do
            ACC := ACC + 1000;
        end
        else
          ShowMessage('No data at ' + IntToStr(CO));
      end;
      if RI[1] = '6' then
      begin
        ACC := ACC * 10;
        while ACC > 999 do
          ACC := ACC - 1000;
      end;
      if RI[1] = '7' then
        ACC := ACC div 10;
      if RI[1] = '8' then
      begin
        if InfoAdr <> '' then
          TMP := StrToInt(InfoAdr)
        else
          ShowMessage('No data at ' + IntToStr(CO));
      end;
      if RI[1] = '9' then
      begin
        CO := StrToInt(RI[2] + RI[3]);
        pasinc := true;
      end;
      if RI[1] = 'A' then
      begin
        if TMP <> ACC then
        begin
          CO := StrToInt(RI[2] + RI[3]);
          pasinc := true;
        end;
      end;
      if RI[1] = 'B' then
      begin
        if ACC > TMP then
        begin
          CO := StrToInt(RI[2] + RI[3]);
          pasinc := true;
        end;
      end;
      if RI[1] = 'C' then
      begin
        if ACC < TMP then
        begin
          CO := StrToInt(RI[2] + RI[3]);
          pasinc := true;
        end;
      end;
      // if RI[1] = 'D' then ;
      // if RI[1] = 'E' then ;
      if RI[1] = 'F' then
        Annuler := true;
      continue := false;
      Application.ProcessMessages;
      if CheckBox1.Checked and (Annuler = false) then
      begin
        Label2.Caption := 'RI : ' + RI;
        Label3.Caption := 'CO : ' + IntToStr(CO);
        Label5.Caption := 'TMP : ' + IntToStr(TMP);
        Label6.Caption := 'ACC : ' + IntToStr(ACC);
        StatusBar1.SimpleText :=
          'Click on "Continue" or type "Enter" to continue';
        Button4.SetFocus;
        while continue = false do
          Application.ProcessMessages;
        StatusBar1.SimpleText := '';
      end;
    end;
  end;
  Run := false;
  ShowMessage('Programme exited !');
end;

procedure TForm1.Button3Click(Sender: TObject);
begin
  if Run then
  begin
    DemandeEntree := false;
    Annuler := true;
  end;
end;

procedure TForm1.Button4Click(Sender: TObject);
begin
  continue := true;
end;

procedure TForm1.Button5Click(Sender: TObject);
var
  t: TStringlist;
  i: Integer;
begin
  if SaveDialog1.Execute then
  begin
    t := TStringlist.Create;
    for i := 0 to 99 do
      t.Add(StringGrid1.Rows[i + 1][1]);
    t.SaveToFile(SaveDialog1.FileName);
    t.Free;
  end;
end;

procedure TForm1.FormDestroy(Sender: TObject);
begin
  cache.Free;
end;

procedure TForm1.Button6Click(Sender: TObject);
var
  i: Integer;
begin
  if cache.Text <> '' then
    for i := 0 to cache.Count - 1 do
      StringGrid1.Rows[i + 1][1] := cache[i];
end;

procedure TForm1.Edit1KeyPress(Sender: TObject; var Key: Char);
begin
  if not(Key in ['0' .. '9', Chr(VK_BACK), Chr(VK_DELETE)]) then
    Key := #0;
end;

procedure TForm1.Button9Click(Sender: TObject);
begin
  if Length(Edit1.Text) < 3 then
    Edit1.Text := Edit1.Text + (Sender as TButton).Caption;
end;

procedure TForm1.Button8Click(Sender: TObject);
begin
  if DemandeEntree then
  begin
    Entree := Edit1.Text;
    Edit1.Text := '';
    DemandeEntree := false;
  end;
end;

procedure TForm1.StringGrid1DrawCell(Sender: TObject; ACol, ARow: Integer;
  Rect: TRect; State: TGridDrawState);
begin
  with Sender as TStringGrid do
    with Canvas do
    begin
      Brush.Color := clWhite;
      if gdFixed in State then
        Brush.Color := clBtnFace;
      if gdSelected in State then
        Brush.Color := clNavy;
      FillRect(Rect);
      if gdSelected in State then
        SetTextColor(Canvas.Handle, clWhite)
      else
        SetTextColor(Canvas.Handle, clBlack);
      DrawText(Canvas.Handle, PChar(Cells[ACol, ARow]), -1, Rect,
        DT_CENTER or DT_NOPREFIX or DT_VCENTER or DT_SINGLELINE);
    end;
end;

end.
