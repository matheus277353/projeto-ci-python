import pytest
from main import calcular_media, situacao_aluno


def test_calcular_media_com_tres_notas():
    assert calcular_media([8.0, 7.0, 9.0]) == 8.0


def test_calcular_media_com_uma_nota():
    assert calcular_media([6.5]) == 6.5


def test_calcular_media_lista_vazia():
    with pytest.raises(ValueError):
        calcular_media([])


def test_situacao_aprovado():
    assert situacao_aluno(7.0) == "Aprovado"


def test_situacao_recuperacao():
    assert situacao_aluno(5.0) == "Recuperação"


def test_situacao_reprovado():
    assert situacao_aluno(4.9) == "Reprovado"
