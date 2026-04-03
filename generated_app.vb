Public Class Form1
    Dim input As String = ""
    Dim operatorSelected As Boolean = False

    Private Sub Button_Click(sender As Object, e As EventArgs) Handles Button0.Click, Button1.Click, Button2.Click, Button3.Click, Button4.Click, Button5.Click, Button6.Click, Button7.Click, Button8.Click, Button9.Click, ButtonDecimal.Click
        Dim button As Button = DirectCast(sender, Button)
        If operatorSelected Then
            TextBox1.Text = ""
            operatorSelected = False
        End If

        TextBox1.Text += button.Text
    End Sub

    Private Sub Operator_Click(sender As Object, e As EventArgs) Handles ButtonAdd.Click, ButtonSubtract.Click, ButtonMultiply.Click, ButtonDivide.Click
        Dim button As Button = DirectCast(sender, Button)
        input = TextBox1.Text
        TextBox1.Text = ""
        operatorSelected = True
    End Sub

    Private Sub ButtonEquals_Click(sender As Object, e As EventArgs) Handles ButtonEquals.Click
        Dim secondInput As Double = Double.Parse(TextBox1.Text)
        Select Case input.Chars(input.Length - 1)
            Case "+"
                TextBox1.Text = Double.Parse(input) + secondInput
            Case "-"
                TextBox1.Text = Double.Parse(input) - secondInput
            Case "*"
                TextBox1.Text = Double.Parse(input) * secondInput
            Case "/"
                TextBox1.Text = Double.Parse(input) / secondInput
        End Select
    End Sub

    Private Sub ButtonClear_Click(sender As Object, e As EventArgs) Handles ButtonClear.Click
        TextBox1.Text = ""
        input = ""
    End Sub
End Class