import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviado_de_email():
    enviador= Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario ',
    ['gelhen@gmail.com', 'foo@bar.com.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'danielarottava@hotmail.com',
        'Cursos Python Pro',
        'Primerira turma Guido Von Rossum Aberta.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario ',
    ['', 'gelhen']
)
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            destinatario,
            'danielarottava@hotmail.com',
            'Cursos Python Pro',
            'Primerira turma Guido Von Rossum Aberta.'
        )