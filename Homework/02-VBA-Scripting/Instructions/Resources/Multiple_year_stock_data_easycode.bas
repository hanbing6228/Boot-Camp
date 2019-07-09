Attribute VB_Name = "Module2"
Sub StockData()

 
  ' LOOP THROUGH ALL SHEETS
   For m = 1 To 3
  
  ' Set an initial variable for holding the Ticker name
   Dim Ticker As String

  ' Set an initial variable for holding the total stock volume
   Dim Total_Stock_Volume As Double
  
   Total_Stock_Volume = 0

  ' Keep track of the location for each stock ticker in the summary table
   Dim Summary_Table_Row As Integer
  
   Summary_Table_Row = 2
  
   ' Automatic caculate all the worksheets
    Worksheets(m).Activate
  
   ' Add the words to the Columns Header
    Cells(1, 10) = "Ticker"
    Cells(1, 13) = "Total Stock Volume"
   
   ' Determine the Last Row
    LastRow = Worksheets(m).Cells(Rows.Count, 1).End(xlUp).Row
  
   ' Loop through all stock data
    For i = 2 To LastRow

   ' Check if we are still within the same Ticker, if it is not...
     If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then

   ' Set the Ticker name
    Ticker = Cells(i, 1).Value

   ' Add to the Total Stock Volume
    Total_Stock_Volume = Total_Stock_Volume + Cells(i, 7).Value

   ' Print the Ticker in the Summary Table
    Range("J" & Summary_Table_Row).Value = Ticker

   ' Print the Totl Stock Volume to the Summary Table
     Range("K" & Summary_Table_Row).Value = Total_Stock_Volume

    ' Add one to the summary table row
      Summary_Table_Row = Summary_Table_Row + 1
      
    ' Reset the Total Stock Volume
      Total_Stock_Volume = 0

    ' If the cell immediately following a row is the same ticker...
      Else

      ' Add
      Total_Stock_Volume = Total_Stock_Volume + Cells(i, 7).Value

        End If

      Next i
  
  
  Next m

End Sub



