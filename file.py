import random
import flet as ft

cp = 0
y=0

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

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
    Exit = ft.ElevatedButton(text="Exit",width =100, on_click=Exit1)
    Rock = ft.ElevatedButton(text="Rock",width =100, on_click=Rock_clicked)
    Paper = ft.ElevatedButton(text="Paper",width =100, on_click=Paper_clicked)
    Scissors = ft.ElevatedButton(text="Scissors",width =100, on_click=Scissors_clicked)

    front_page = ft.Container(
    content=ft.Column(
        [
            ft.Text("Welcome to Rock, Paper, Scissors"),
            ft.ElevatedButton(text="Start Game", on_click=Start_game)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    ),
    alignment=ft.alignment.center,
    visible=True
)
    game_page = ft.Container(
    content=ft.Column(
        [
            ft.Row(
                [
                    ft.Column(
                        controls=[Rock, Paper, Scissors],
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    ft.Column(
                        controls=[Comp],
                       alignment=ft.MainAxisAlignment.START,
                       horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                
            ),
           ft.Row(
               controls=[ output_text,
                         Text,
                         Score,
                         Exit],
              alignment=ft.MainAxisAlignment.CENTER,
             #horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ), 
        ]
    ),
      
                     
    alignment=ft.alignment.center,
    visible=False
)
    page.add(front_page,game_page)

ft.app(target=main,view=ft.AppView.WEB_BROWSER)


