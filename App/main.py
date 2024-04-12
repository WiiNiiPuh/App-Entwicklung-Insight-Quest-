
#Liberies 
from kivy.lang import Builder
from kivy.properties import StringProperty


from kivymd.app import MDApp
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard



class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()


class CheckScreen(MDScreen):
    image_size = StringProperty()

class WeekScreen(MDScreen): 
    image_size = StringProperty()
    icon = StringProperty()
    text = StringProperty() # Add this line

class TeamScreen(MDScreen):
    image_size = StringProperty()

class MyCard(MDCard):
    '''Implements a material card.'''

    text = StringProperty()



KV = """

<BaseMDNavigationItem>

    MDNavigationItemIcon:
        icon: root.icon

    MDNavigationItemLabel:
        text: root.text
    


<CheckScreen>

    MDLinearProgressIndicator:
        id: progress
        size_hint_x: .5
        type: "determinate"
        pos_hint: {'center_x': .5, 'center_y': .8}

    MDButton:
        style: "elevated"
        pos_hint: {"center_x": .5, "center_y": .7}
        
        MDButtonIcon:
            icon: "read"
        MDButtonText:
            text: "Lesen"

    MDButton:
        style: "elevated"
        pos_hint: {"center_x": .5, "center_y": .6}
        
        MDButtonIcon:
            icon: "meditation"
        MDButtonText:
            text: "Meditation"

    MDButton:
        style: "elevated"
        pos_hint: {"center_x": .5, "center_y": .5}
        

        MDButtonIcon:
            icon: "weight-lifter"
        MDButtonText:
            text: "Sport"

<WeekScreen>
    MDBoxLayout:
        id: box
        adaptive_size: True
        spacing: "12dp"
        orientation: 'vertical'

        pos_hint: {"center_x": .5, "center_y": .5}

        MyCard:
            padding: "4dp"
            size_hint: None, None
            size: "240dp", "100dp"
            style: "filled"

            MDRelativeLayout:

                MDIconButton:
                    icon: "dots-vertical"
                    pos_hint: {"top": 1, "right": 1}

                MDLabel:
                    text: "20 cm"
                    color: "black"
                    pos: "12dp", "12dp"          

                MDLabel:
                    text: "Lukas Penis"
                    adaptive_size: True
                    color: "grey"
                    pos: "12dp", "12dp"
                    bold: True    
        
        MDCard:
            style: "elevated"
            pos_hint: {"center_x": .5, "center_y": .4}
            padding: "4dp"
            size_hint: None, None
            size: "240dp", "200dp"

            MDRelativeLayout:

                MDIconButton:
                    icon: "dots-vertical"
                    pos_hint: {"top": 1, "right": 1}

                FitImage:
                    source: "/Volumes/HDD - Daten/Python/KIVY Tutorials/MeinMoMoAppVersuch/imgbin_sex-position-jigsaw-puzzles-sexual-intercourse-man-doggy-style-png.png"
                    size_hint_y: .75
                    pos_hint: {"top": 1}
                    radius: "36dp", "36dp", 0, 0
                
                MDLabel:
                    text: "Buche jetzt einen Termin"
                    color: "black"
                    pos_hint: {"center_x": .5, "center_y": .4}   

                MDLabel:
                    text: "Hab Sex mit Lukas"
                    adaptive_size: True
                    color: "grey"
                    pos: "12dp", "12dp"
                    bold: True

<TeamScreen>

    MDBoxLayout:
        id: box
        spacing: "12dp"
        orientation: 'vertical'

        MDListItem:
            pos_hint: {"center_x": .5, "center_y": .5}

            MDListItemLeadingIcon:
                icon: "trophy-award"

            MDListItemHeadlineText:
                text: "TEAM-GOALS"

            MDListItemSupportingText:
                text: "Lukas gibt uns einen Lapdance"

            MDListItemTertiaryText:
                text: "Bei erreichen von 30 Punkten"

            MDListItemTrailingCheckbox:

        MDListItem:
            pos_hint: {"center_x": .5, "center_y": .3}

            MDListItemLeadingIcon:
                icon: "trophy-award"

            MDListItemHeadlineText:
                text: "TEAM-GOALS"

            MDListItemSupportingText:
                text: "Truc backt allen Kuchen "

            MDListItemTertiaryText:
                text: "Bei erreichen von 15 Punkten"

            MDListItemTrailingCheckbox:

        MDListItem:
            pos_hint: {"center_x": .5, "center_y": .7}

            MDListItemLeadingIcon:
                icon: "trophy-award"

            MDListItemHeadlineText:
                text: "TEAM-GOALS"

            MDListItemSupportingText:
                text: "Alex erstes Sextape"

            MDListItemTertiaryText:
                text: "Bei erreichen von 60 Punkten"

            MDListItemTrailingCheckbox:



MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: self.theme_cls.backgroundColor

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    type: "small"
                    size_hint_x: .8
                    pos_hint: {"center_x": 1, "center_y": .9}

                    MDTopAppBarLeadingButtonContainer:

                        MDActionTopAppBarButton:
                            icon: "arrow-left"
                            on_release: nav_drawer.set_state("toggle")
                        
                MDTopAppBarTitle:
                    text: "Base"
                    pos_hint: {"center_x": .5, "center_y": .9}

                MDTopAppBarTrailingButtonContainer:

                    MDActionTopAppBarButton:
                        icon: "account-circle-outline"
                        pos_hint: {"center_x": .2, "center_y": .9}
                
                MDScreenManager:
                    id: screen_manager

                    CheckScreen:
                        name: "Check heute"
                        

                    WeekScreen:
                        name: "Week View"
                        

                    TeamScreen:
                        name: "TEAM-Goals"
                        

                    
                MDNavigationBar:
                    on_switch_tabs: app.on_switch_tabs(*args)

                    BaseMDNavigationItem
                        icon: "check-circle"
                        text: "Check heute"
                        active: True

                    BaseMDNavigationItem
                        icon: "calendar"
                        text: "Week View"

                    BaseMDNavigationItem
                        icon: "matrix"
                        text: "TEAM-Goals"

                        
    MDNavigationDrawer:
        id: nav_drawer
        radius: 0, dp(16), dp(16), 0

        MDNavigationDrawerMenu:

            MDNavigationDrawerLabel:
                text: "Navigation"

            MDNavigationDrawerItem:

                MDNavigationDrawerItemLeadingIcon:
                    icon: "home"

                MDNavigationDrawerItemText:
                    text: "Home"


            MDNavigationDrawerDivider:





"""


class BaseScreen(MDApp):

    def on_press(self): 
        pass

    def on_switch_tabs(
        self,
        bar: MDNavigationBar,
        item: MDNavigationItem,
        item_icon: str,
        item_text: str,
    ):
        self.root.ids.screen_manager.current = item_text

    def build(self):
        self.theme_cls.primary_palette = "Green" 
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)
    
    # def on_start(self):
    #     super().on_start()
    #     # Assuming you want to add widgets to the BoxLayout in the WeekScreen
    #     week_screen = self.root.ids.screen_manager.get_screen('Week View')
    #     if week_screen:
    #         for style in ("elevated", "filled", "outlined"):
    #             week_screen.ids.box.add_widget(
    #                 MyCard(style=style, text=style.capitalize())
                # )


BaseScreen().run()