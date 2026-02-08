import flet as ft

def main(page: ft.Page):


    page.title = "Calculadora TAP"
    page.window_width = 250
    page.window_height = 400
    page.padding = 20


    display_text = ft.Text("0",color=ft.Colors.WHITE,size=30)
    display = ft.Container (
        content=display_text,
        bgcolor=ft.Colors.BLACK12,
        border_radius=8,
        alignment=ft.alignment.Alignment(1, 0),
        padding=10,
        width=210,
        height=70,
       )
    
    def button_clicked(e: ft.ControlEvent):
      value = e.control.data
      print(f"Button clicked with data = {value}")
      if value == "AC":
        display_text.value = "0"
      if value == "1":
         display_text.value+="1"     
      if value == "2":
         display_text.value+="2"
      if value == "3":
         display_text.value+="3"

      page.update()

    grid = ft.GridView(
        runs_count=2,
        spacing=10,
        run_spacing=10,
        width=210,
        height=210,
        expand=False
    )

    grid.controls.append(
        ft.Container(
            ft.Button("1",data="1",on_click=button_clicked),
            height=50, 
            bgcolor=ft.Colors.PURPLE_100, 
            border_radius=8),
            )
    grid.controls.append(
        ft.Container(
            ft.Button("2",data="2",on_click=button_clicked),
            height=50,
            bgcolor=ft.Colors.LIGHT_BLUE_100, 
            border_radius=8
            ))
    grid.controls.append(
        ft.Container(
            ft.Button("3",data="3",on_click=button_clicked),
            height=50, 
            bgcolor=ft.Colors.AMBER_100,
            border_radius=8))
    grid.controls.append(
        ft.Container(
            ft.Button("AC",data="AC",on_click=button_clicked),
            height=50,
            bgcolor=ft.Colors.GREEN_100,
            border_radius=8))
    
    layout_principal = ft.Column(
        controls=[
            display,
            grid   
        ],
        tight=True
    )


    page.add(layout_principal)
    page.update()
ft.app(target=main)
