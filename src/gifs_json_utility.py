import json


# ------------------------------------------------------ #
# - This is an utility to generate the gifs.json file. - #
# - The keys should only be 'funny' and 'crazy'.       - #
# ------------------------------------------------------ #


gifs = open('gifs.json', 'w')

gifs_dict = {
    'funny': [
        'https://media.tenor.com/5lLcKZgmIhgAAAAC/american-psycho-patrick-bateman.gif',
        'https://media.tenor.com/xV70qxxgM14AAAAC/patrick-bateman.gif',
        'https://media.tenor.com/nogVc6m0iYUAAAAC/american-psycho-christian-bale.gif',
        'https://media.tenor.com/Zd4fex5jsoYAAAAC/american-psycho-patrick-bateman.gif',
        'https://media.tenor.com/CwKLkG69yfMAAAAd/patrick-bateman-american-psycho.gif',
        'https://media.tenor.com/cKkNLp8vVBEAAAAC/patrick-bateman-american-psycho.gif',
        'https://media.tenor.com/gkLlgAaNrI8AAAAC/patrick-bateman-american-psycho.gif',
        'https://media.tenor.com/PLL_Hgq-ezsAAAAd/american-psycho-impressive.gif',
        'https://media.tenor.com/so2gILymRJ0AAAAC/yes-christianbale.gif'
    ],
    'crazy': [
        'https://media.tenor.com/ikvEMCIBsJUAAAAd/patrick-bateman-stare-into-your-soul.gif',
        'https://media.tenor.com/Q823-830Ri0AAAAd/christian-bale-american-psycho.gif',
        'https://media.tenor.com/ykcWZA1_r80AAAAC/sleepy-christian-bale.gif',
        'https://media.tenor.com/41mF6mkjbeAAAAAd/bateman-patrick.gif',
        'https://media.tenor.com/2U_hdX_TSCMAAAAd/patrick-bateman-stare.gif',
        'https://media.tenor.com/Xi3lXyCsai8AAAAd/american-psycho-patrick-bateman.gif',
        'https://media.tenor.com/Py5fYTbsfakAAAAd/patrick-bateman.gif',
        'https://media.tenor.com/cmWMoi_lEf0AAAAd/american-psycho-sigma.gif',
        'https://media.tenor.com/_ddLI4byYTYAAAAd/patrick-bateman-american-psycho.gif',
        'https://media.tenor.com/Pukf2xQnY0QAAAAd/christian-bale-patrick-bateman.gif',
        'https://media.tenor.com/n_68o_314P0AAAAd/patrick-bateman-worried.gif',
        'https://media.tenor.com/wjzOO-ln1CwAAAAd/american-psycho-axe.gif',
        'https://media.tenor.com/icFB4ogOwbYAAAAd/patrick-bateman-sigma.gif',
        'https://media.tenor.com/GGcCRvftHigAAAAd/patrick-bateman-american-psycho.gif',
        'https://media.tenor.com/lHqStSN1qBoAAAAC/patrick-bateman-insane.gif',
        'https://media.tenor.com/mMhK3b1I2bYAAAAC/christian-bale.gif',
        'https://media.tenor.com/gKjoY08UUTEAAAAd/patrick-bateman-american-psycho.gif',
        'https://media.tenor.com/o2CC0IGr7IoAAAAd/american-americanpsycho.gif',
        'https://media.tenor.com/dxHHcZYWB4QAAAAC/peeling-peeling-face.gif',
        'https://media.tenor.com/UvIoEPg-Wl0AAAAC/hyunjin-loona.gif',
        'https://media.tenor.com/1szXFI67iWYAAAAd/patrick-bateman-american-psycho-smoke.gif',
        'https://media.tenor.com/2HnxIhkQ_UAAAAAd/patrick-bateman.gif'
    ]
}

json.dump(gifs_dict, gifs)
gifs.close()
