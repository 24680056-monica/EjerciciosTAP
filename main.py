import flet as ft

def main(page: ft.Page):


    page.title = "Calculadora TAP"
    page.window_width = 250
    page.window_height = 400
    page.padding = 20

    display = ft.Container (
        content=ft.Text("0",color=ft.Colors.WHITE,size=30),
        bgcolor=ft.Colors.BLACK12,
        border_radius=8,
        alignment=ft.alignment.Alignment(1, 0),
        padding=10,
        width=210,
        height=70,
       )


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
            ft.Button("1"), 
            height=50, 
            bgcolor=ft.Colors.PURPLE_100, 
            border_radius=8)
            )
    grid.controls.append(
        ft.Container(
            ft.Button("2"),
            height=50,
            bgcolor=ft.Colors.LIGHT_BLUE_100, 
            border_radius=8
            ))
    grid.controls.append(
        ft.Container(
            ft.Button("3"),
            height=50, 
            bgcolor=ft.Colors.AMBER_100,
            border_radius=8))
    grid.controls.append(
        ft.Container(
            ft.Button("AC"),
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
