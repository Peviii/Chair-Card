from flet import *

def main(page: Page):
    page.title='Chair Card'
    page.window.width=800
    page.window.height=800
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.bgcolor='#000000'
    page.scroll=ScrollMode.AUTO,

    def change_main_img(e):
        for element in options.controls:
            if element == e.control:
                element.opacity = 1
                main_image.src = element.image_src
            else:
                element.opacity = 0.5
        main_image.update()
        options.update()

    product_images = Container(
        col={'xs': 12, 'md': 6},
        bgcolor=colors.WHITE,
        padding=padding.all(30),
        aspect_ratio=9/16,
        content=Column(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                main_image := Image(
                    src='https://imgs.ponto.com.br/1555947067/1xg.jpg'
                ),
                options := Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Container(
                            image_src='https://imgs.ponto.com.br/1555947055/1xg.jpg',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_img,
                        ),
                        Container(
                            image_src='https://imgs.ponto.com.br/1555947067/1xg.jpg',
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_img,
                        ),
                        Container(
                            image_src='https://imgs.ponto.com.br/1555947069/1xg.jpg',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_img,
                        ),
                        
                    ]
                )
            ]
        )
    )
    product_details = Container(
        col={'xs': 12, 'md': 6},
        padding=padding.all(30),
        bgcolor=colors.BLACK87,
        aspect_ratio=9/16,
        content = Column(
            controls=[
                Text(
                    value='CADEIRAS',
                    color=colors.AMBER,
                    weight=FontWeight.BOLD,
                ),
                Text(
                    value='Poltronas Modernas',
                    color=colors.WHITE,
                    weight=FontWeight.BOLD,
                    size=30,
                ),
                Text(value='sala de estar', color=colors.GREY, italic=True),
                ResponsiveRow(
                    columns=12,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Text(
                            col={'xs': 12, 'sm': 6},
                            value='R$ 399',
                            color=colors.WHITE,
                            size=30,
                        ),
                        Row(
                            col={'xs': 12, 'sm': 6},
                            wrap=False,
                            controls=[
                                Icon(
                                    name=icons.STAR,
                                    color=colors.AMBER if _ < 4 else colors.WHITE,
                                ) for _ in range(5)
                            ]
                        )
                    ]
                ),
                Tabs(
                    selected_index=0,
                    height=150,
                    indicator_color=colors.AMBER,
                    label_color=colors.AMBER,
                    tabs=[
                        Tab(
                            text='Descrição',
                            content=Container(
                                padding=padding.all(10),
                                content=Text(
                                    value='As melhores opções de poltronas para sala de estar, com design minimalista, e cores suaves, perfeitas para o comodo de seu lar.',
                                    color=colors.GREY,
                                )
                            )
                        ),
                        Tab(
                            text='Detalhes',
                            content=Text(
                                    value='Dimensões: 0.8m de largura, 0.9m de altura e 0.76m de profundidade',
                                    color=colors.GREY,
                                )
                        ),
                    ]
                ),
                ResponsiveRow(
                    columns=12,
                    controls=[
                        Dropdown(
                            col=6,
                            label='Cor',
                            label_style=TextStyle(color=colors.WHITE, size=16),
                            border_color=colors.GREY,
                            border_width=0.5,
                            options=[
                                dropdown.Option(text='Amarelo'),
                                dropdown.Option(text='Vermelho'),
                                dropdown.Option(text='Azul'),
                            ]
                        ),
                        Dropdown(
                            col=6,
                            label='Quantidade',
                            label_style=TextStyle(color=colors.WHITE, size=16),
                            border_color=colors.GREY,
                            border_width=0.5,
                            options=[
                                dropdown.Option(text=f'{num} unidade(s)') for num in range(1, 11)                                
                            ]
                        ),
                    ]
                ),
                Container(expand=True),
                ElevatedButton(
                    width=900,
                    text='Adicionar a lista de desejos',
                    style=ButtonStyle(
                        padding=padding.all(20),
                        side={
                            ControlState.DEFAULT: BorderSide(width=2, color=colors.WHITE)
                        },
                        bgcolor={
                            ControlState.HOVERED: colors.WHITE
                        },
                        color={
                            ControlState.DEFAULT: colors.WHITE,
                            ControlState.HOVERED: colors.BLACK
                        }
                    )
                ),
                ElevatedButton(
                    width=900,
                    text='Adicionar ao carrinho',
                    style=ButtonStyle(
                        padding=padding.all(20),
                        side={
                            ControlState.DEFAULT: BorderSide(width=2, color=colors.AMBER)
                        },
                        bgcolor={
                            ControlState.DEFAULT: colors.AMBER
                        },
                        color={
                            ControlState.DEFAULT: colors.AMBER,
                            ControlState.DEFAULT: colors.BLACK
                        }
                    )
                ),
            ]
        )
    )
    layout = Container(
        width=900,
        margin=margin.all(30),
        shadow=BoxShadow(blur_radius=300, color=colors.CYAN),
        content=ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls={
                product_images,
                product_details,
            }
        ),
    )

    page.add(layout)

    

app(target=main)
