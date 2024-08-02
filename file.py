import random
import flet as ft

cp = 0
y=0

def main(page: ft.Page):
    def Exit1(e):
        Rock.visible = False
        Paper.visible = False
        Scissors.visible = False
        output_text.value = ""
        Text.value = ""
        Score.value = f"Your score={y}\nComputer Score={cp}"
        Comp.text = "Game Exited"
        Exit.visible = False
        page.update()
    
    def Scores(): 
        Score.value = f"Your score={y}\nComputer Score={cp}"
        page.update()
    
    def Computer():
        Elements=[1,2,3]
        CChoice = ["Rock","Paper","Scissors"]
        C = random.choice(Elements)
        Comp.text = CChoice[C-1]
        page.update()
        return C
    
    
    def Rock_clicked(e):
        global cp,y
        Computer1 = Computer()
        output_text.value = "Your choice is Rock"
        if Computer1 == 1 :
            Text.value="Similar choice"
        elif Computer1 == 2 :
            Text.value="Computer wins"
            cp+=1
        else :
            Text.value="You win"
            y+=1
        Scores()
        page.update()
   
    def Paper_clicked(e):
        global cp,y
        Computer1 = Computer()
        output_text.value ="Your choice is Paper"
        if Computer1 == 2 :
            Text.value="Similar choice"
        elif Computer1 == 3 :
            Text.value="Computer wins"
            cp+=1
        else :
            Text.value="You win"
            y+=1
        Scores()
        page.update()
    
    
    def Scissors_clicked(e):
        global cp,y
        output_text.value ="Your choice is Scissors"
        Computer1 = Computer()
        if Computer1 == 3 :
            Text.value="Similar choice"
        elif Computer1 == 1 :
            Text.value="Computer wins"
            cp+=1
        else :
            Text.value="You win"
            y+=1
        Scores()
        page.update()
    
    def Start_game(e):
        front_page.visible = False
        game_page.visible = True
        page.update()

    output_text = ft.Text()
    Text = ft.Text()
    Score = ft.Text()
    Comp = ft.ElevatedButton(text=" ")
    Exit = ft.ElevatedButton(text="Exit", on_click=Exit1)
    Rock = ft.ElevatedButton(text="Stone", on_click=Rock_clicked)
    Paper = ft.ElevatedButton(text="Paper", on_click=Paper_clicked)
    Scissors = ft.ElevatedButton(text="Scissors", on_click=Scissors_clicked)

    front_page = ft.Column(
        controls =[
            ft.Text("Welcome to Rock,Paper,Scissors"),
            ft.ElevatedButton(text="Start Game",on_click=Start_game)
        ],
        visible=True
    )
    game_page = ft.Column(
        controls =[
            Rock,Paper,Scissors,output_text,Text,Score,Comp,Exit
        ],
        visible = False
    )
#    color_dropdown = ft.Dropdown(
#        width=100,
#        options=[
#            ft.dropdown.Option("Red"),
#            ft.dropdown.Option("Green"),
#            ft.dropdown.Option("Blue"),
#        ],
#    )
    page.add(front_page,game_page)

ft.app(target=main,view=ft.AppView.WEB_BROWSER)


