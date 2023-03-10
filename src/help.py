from discord import Embed
from typing import List


def get_help() -> List[Embed]:
    embeds = []
    # Page 1
    embed_1 = Embed(color=0x3a86ff)
    embed_1.title = 'Contador de Surtos'
    embed_1.description = 'Página de ajuda'
    embed_1.add_field(name='Descrição',
        value='Contador de Surtos é um bot feito com o intuito de, '\
        'como o próprio nome sugere, contar os surtos dos membros de um servidor. '\
        'Todos os dias, o contador informa estatísticas sobre os surtos contabilizados. '\
        'Essa página guia o usuário pelos comandos disponíveis pelo bot.',
        inline=False)
    embeds.append(embed_1)
    # Page 2
    embed_2 = Embed(color=0x3a86ff)
    embed_2.title = 'Contador de Surtos'
    embed_2.description = 'Página de ajuda'
    embed_2.add_field(name='Adicionar um surto',
        value='Para adicionar um surto, o comando **>surto** deve ser utiizado. Sua sintaxe é a seguinte:\n\n'\
        '**>surto** *motivo do surto*\n\n'\
        'Assim, o surto será armazenado juntamente com sua data e horário de adição. '\
        'Caso necessário, esse surto pode ser removido a qualquer momento.',
        inline=False)
    embeds.append(embed_2)
    # Page 3
    embed_3 = Embed(color=0x3a86ff)
    embed_3.title = 'Contador de Surtos'
    embed_3.description = 'Página de ajuda'
    embed_3.add_field(name='Mostrar o histórico de surtos',
    value='Com o comando **>surtos**, é possível receber o histórico completo de surtos, sua sintaxe é:\n\n'
        '**>surtos**\n\n'\
        'Como pode ser observado, o comando não recebe argumentos. Para navegar entre as páginas, '\
        'basta tocar nos ícones que apontam para esquerda ou para a direita para, respectivamente, '
        'ser direcionado à página anterior ou à próxima página.',
    inline=False)
    embeds.append(embed_3)
    # Page 4
    embed_4 = Embed(color=0x3a86ff)
    embed_4.title = 'Contador de Surtos'
    embed_4.description = 'Página de ajuda'
    embed_4.add_field(name='Estatísticas de surtos',
    value='Pelo comando **>stats**, é possível receber uma mensagem com estatísticas sobre o histórico de surtos, '\
        'sua sintaxe é:\n\n'
        '**>stats**\n\n'\
        'O comando não recebe argumentos. Com isso, as estatísticas serão enviadas em uma simples mensagem.',
    inline=False)
    embeds.append(embed_4)
    # Page 5
    embed_5 = Embed(color=0x3a86ff)
    embed_5.title = 'Contador de Surtos'
    embed_5.description = 'Página de ajuda'
    embed_5.add_field(name='Remover um surto',
    value='Usando o comando **>remove**, qualquer surto do histórico pode ser removido permanentemente, '\
        'sua sintaxe é:\n\n'
        '**>remove**\n\n'\
        'O comando não recebe argumentos. Uma vez invocado, o comando mostrará o histórico de surtos e '\
        'esperará por uma mensagem contendo o índice do surto a ser removido. '\
        'Uma vez digitado um índice válido, o surto a ser removido será mostrado e, ainda, será necessária '\
        'confirmação do usuário, que acontece ao enviar uma mensagem somente com a letra **y**.',
    inline=False)
    embeds.append(embed_5)
    # Page 6
    embed_6 = Embed(color=0x3a86ff)
    embed_6.title = 'Contador de Surtos'
    embed_6.description = 'Página de ajuda'
    embed_6.add_field(name='Redefinir o bot',
    value='Usando o comando **>reset**, todos os dados do bot podem ser redefinidos apagando todo o seu histórico, '\
        'sua sintaxe é:\n\n'
        '**>reset** *ID*\n\n'\
        'Onde *ID* corresponde ao ID do servidor atual. Uma vez que um ID válido seja fornecido, o bot confirmará '
        'a redefinição de todos os seus dados.',
    inline=False)
    embeds.append(embed_6)
    # Page 7
    embed_7 = Embed(color=0x3a86ff)
    embed_7.title = 'Contador de Surtos'
    embed_7.description = 'Página de ajuda'
    embed_7.add_field(name='Canal de texto, cargo, e permissões',
    value='O bot, por via de regra, cria o canal de texto *contador-de-surtos*, que será destinado aos seus avisos '\
        'diários. Além disso, também é criado o cargo *Gerente de Surtos*, que deve ser usado para designar os '\
        'usuários com permissões especiais com relação ao bot. Não há como alterar esse comportamento. Abaixo, '\
        'segue a lista de permissões exigidas para cada comando:\n\n'\
        '**>surto** - Gerente de Surtos\n'\
        '**>surtos** - Sem permissões especiais\n'\
        '**>stats** - Sem permissões especiais\n'\
        '**>remove** - Gerente de Surtos\n'\
        '**>reset** - Apenas administradores\n'\
        '**>help** - Sem permissões especiais\n\n'\
        'Administradores têm acesso a todos os comandos, independentemente do requerimento de cargo.',
    inline=False)
    embeds.append(embed_7)
    return embeds
