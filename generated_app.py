```vb
Imports System.ComponentModel

Public Class CalculatorForm
    Private operation As String = ""
    Private firstOperand As Double = 0
    Private secondOperand As Double = 0

    Private Sub numberButton_Click(sender As Object, e As EventArgs) Handles btn0.Click, btn1.Click, btn2.Click, btn3.Click, btn4.Click, btn5.Click,
        btn6.Click, btn7.Click, btn8.Click, btn9.Click
        Dim button As Button = DirectCast(sender, Button)
        If txtDisplay.Text = "0" OrElse isOperandSet() Then
            txtDisplay.ResetText()
        End If
        txtDisplay.Text += button.Text
    End Sub

    Private Function isOperandSet() As Boolean
        Return txtDisplay.Text <> "" AndAlso Not txtDisplay.Text.EndsWith(".") AndAlso Not txtDisplay.Text.EndsWith("E")
    End Function

    Private Sub decimalButton_Click(sender As Object, e As EventArgs) Handles btnDecimal.Click
        If Not txtDisplay.Text.Contains(".") Then
            txtDisplay.Text += "."
        End If
    End Sub

    Private Sub operationButton_Click(sender As Object, e As EventArgs) Handles btnAdd.Click, btnSubtract.Click, btnMultiply.Click, btnDivide.Click
        Dim button As Button = DirectCast(sender, Button)
        operation = button.Text
        firstOperand = Double.Parse(txtDisplay.Text)
        txtDisplay.ResetText()
    End Sub

    Private Sub clearButton_Click(sender As Object, e As EventArgs) Handles btnClear.Click
        operation = ""
        firstOperand = 0
        txtDisplay.ResetText()
    End Sub

    Private Sub equalsButton_Click(sender As Object, e As EventArgs) Handles btnEquals.Click
        secondOperand = Double.Parse(txtDisplay.Text)
        Select Case operation
            Case "+"
                txtDisplay.Text = (firstOperand + secondOperand).ToString()
            Case "-"
                txtDisplay.Text = (firstOperand - secondOperand).ToString()
            Case "*"
                txtDisplay.Text = (firstOperand * secondOperand).ToString()
            Case "/"
                txtDisplay.Text = (firstOperand / secondOperand).ToString()
        End Select
    End Sub

    Private Sub CalculatorForm_Closing(sender As Object, e As CancelEventArgs) Handles Me.Closing
        Application.Exit()
    End Sub
End Class
```