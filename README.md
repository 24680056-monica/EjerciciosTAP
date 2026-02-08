Inicio de una interfaz de calculadora <br>
Antes de mostrar el desarrollo de la interfaz la cual se muestra a traves de Flet, por lo que se realiza la instalacion de este<br>
creando un entorno virtual a traves de Git Bash, asi que inicialmente  se genera una una carpeta donde ahi se implementara Flet:
```bash
mkdir my-app
cd my-app
```
 Una vez que se haya creado se activa el entorno virtual
```bash
py -m venv .venv  
source .venv/Scripts/activate
```
Finalmente, se instala Flet despues de activar el entorno virtual
```bash
pip install 'flet[all]'
```
Y despues, se verificar que se haya instalado correctamente
```bash
flet --version
```
Despues de crear la dependencia aislada de Flet, se abre Visual Studio Code en la carpeta que creamos previamente donde ahi esta importado Flet.<br>
Inicialmente, se generara la pagina donde se mostrara la calculadora:
```python
import flet as ft

def main(page: ft.Page):


    page.title = "Calculadora TAP"
    page.window_width = 250
    page.window_height = 400
    page.padding = 20
```
Aqui se dan los valores del ancho y alto que tendra la ventana que se abrira y su titulo que mostrara, en este caso sera el de "Calculadora TAP" y la distancia que tendra nuestra vista de los botones con la ventana. <br>
Ahora se agrega la parte donde se visualizaran los numeros o valores que se presionen segun el boton:
```python
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
```
En esta parte, inicialmente se coloca la variable del texto que mostrara y sus componente, despues se crea el display (donde se visualizara) y colocando lo que contendra como los colores, ancho, altura, color y el texto que mostrara.
Posteriormente, se agrega la funcion de los botones donde se les podra dar click y asignaran un valor el cual se mostrara en el display que se genero previamente:
```python
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
```
En esta parte genera la funcion de los botones donde se les dara el evento que recibiran, asignando una variable la cual recibira el evento con los datos segun el el boton presionando o clickeado, se agrego un print para mostrar en la terminar y verificar que se este haciendo correctamente, por otro lado, se agregaron las condiciones, segun el boton que se presione es el valor que dara y mostrara ademas de que se agregaran o si presionan la tecla AC, se borraran los datos anteriores y se mostrara 0, el page update servira para actualizar los datos o lo que se mostrara.
Ahora, se agregara la parte donde se mostraran los botones.
```python
    grid = ft.GridView(
        runs_count=2,
        spacing=10,
        run_spacing=10,
        width=210,
        height=210,
        expand=False
    )
```
En esta parte simplemente se dan los componentes del espacio, altura y ancho u expansion.
Por consiguiente, se agregaran los botones donde a cada uno se le colocaran sus componentes o lo que llevara cara uno.
```python
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
```
Se agregan 4 botones por el momento, conteniendo los numeros del 1 al 3 y el AC para borrar, los botones contienen por el momento lo principal, el valor que mostrara y el dato que asiganara o dara si le dan click ademas que se le agrego esa funcion, se les dio una altura, un color distinto cada uno y finalmente su borde.
Por ultimo, se generara nuestra parte principal donde tendra dentro grid (la parte donde se muestran los botones) y el display (donde se muestran los valores segun le des click a los botones). Una vez hecho eso se agregan en la pagina donde dentro tendra la variable principal que tiene dentro el grid y display, ademas de dar un page.update:
```python
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
```
el ft.app que se muestra al final es lo que permite que se corra el programa.
En conjunto de todo, lo siguiente es el codigo completo:
```Python
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
```
A continuacion se visualiza el resultado de todo el codigo: <br>
<img width="312" height="483" alt="image" src="https://github.com/user-attachments/assets/726581f1-b4e1-4364-baa1-982334e2412e" />


