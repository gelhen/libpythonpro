from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpan
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Gelhen', email='gelhen@gmail.com'),
            Usuario(nome='Andre', email='andre@gmail.com')
        ],
        [
            Usuario(nome='Gelhen', email='gelhen@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpan(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gelhen@gmail.com',
        'Curso_paython Pro',
        'Confira_os moduloa fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Gelhen', email='gelhen@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpan(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'andre@gmail.com',
        'Curso_paython Pro',
        'Confira_os moduloa fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'andre@gmail.com',
        'gelhen@gmail.com',
        'Curso_paython Pro',
        'Confira_os moduloa fantásticos'
    )