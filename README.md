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
