import discord
from collections import deque
from typing import List


class PaginatorView(discord.ui.View):
    def __init__(self, embeds: List[discord.Embed]) -> None:
        super().__init__(timeout=30)
        self.embeds = embeds
        self.pages = deque(embeds)
        self.first_page = embeds[0]
        self.len = len(embeds)
        self.current_page = 1
        self.children[0].disabled = True
        self.pages[0].set_footer(text=f'Página {self.current_page} de {self.len}.')
        if self.current_page == self.len:
            self.children[1].disabled = True

    async def update_buttons(self, interaction: discord.Interaction):
        self.pages[0].set_footer(text=f'Página {self.current_page} de {self.len}.')
        if self.current_page == 1:
            self.children[0].disabled = True
        else:
            self.children[0].disabled = False
        if self.current_page == self.len:
            self.children[1].disabled = True
        else:
            self.children[1].disabled = False
        await interaction.edit_original_response(view=self)

    @discord.ui.button(emoji='\N{WHITE LEFT POINTING BACKHAND INDEX}')
    async def previous_page(self, interaction: discord.Interaction, _) -> None:
        self.pages.rotate(1)
        new_page = self.pages[0]
        self.current_page -= 1
        await interaction.response.edit_message(embed=new_page)
        await self.update_buttons(interaction)

    @discord.ui.button(emoji='\N{WHITE RIGHT POINTING BACKHAND INDEX}')
    async def next_page(self, interaction: discord.Interaction, _) -> None:
        self.pages.rotate(-1)
        new_page = self.pages[0]
        self.current_page += 1
        await interaction.response.edit_message(embed=new_page)
        await self.update_buttons(interaction)

    @property
    def starting_page(self) -> discord.Embed:
        return self.first_page

