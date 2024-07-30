import random
import flet as ft


def main(page: ft.Page):
    def Computer():
        Elements=[1,2,3]
        return random.choices(Elements)
    def Rock_clicked(e):
        output_text.value = "Your choice is Rock"
        if Computer == 1 :
            Text.value="Similar choice"
        elif Computer == 2 :
            Text.value="Computer wins"
        else :
            Text.value="You win"
        page.update()
    def Paper_clicked(e):
        output_text.value ="Your choice is Paper"
        if Computer == 2 :
            Text.value="Similar choice"
        elif Computer == 3 :
            Text.value="Computer wins"
        else :
            Text.value="You win"
        page.update()
    def Scissors_clicked(e):
        output_text.value ="Your choice is Scissors"
        if Computer == 3 :
            Text.value="Similar choice"
        elif Computer == 1 :
            Text.value="Computer wins"
        else :
            Text.value="You win"
        page.update()
    

    output_text = ft.Text()
    Text = ft.Text()
    Rock = ft.ElevatedButton(text="Stone", on_click=Rock_clicked)
    Paper = ft.ElevatedButton(text="Paper", on_click=Paper_clicked)
    Scissors = ft.ElevatedButton(text="Scissors", on_click=Scissors_clicked)
#    color_dropdown = ft.Dropdown(
#        width=100,
#        options=[
#            ft.dropdown.Option("Red"),
#            ft.dropdown.Option("Green"),
#            ft.dropdown.Option("Blue"),
#        ],
#    )
    page.add( Rock, Paper, Scissors, output_text,Text)

ft.app(target=main,view=ft.AppView.WEB_BROWSER)


