def calcular_media(notas: list[float]) -> float:
    """Retorna a média das notas informadas."""
    if not notas:
        raise ValueError("A lista de notas não pode estar vazia.")
    return sum(notas) / len(notas)


def situacao_aluno(media: float) -> str:
    """Classifica o aluno a partir de sua média final."""
    if media >= 7:
        return "Aprovado"
    if media >= 5:
        return "Recuperação"
    return "Reprovado"


if __name__ == "__main__":
    notas_exemplo = [8.0, 7.0, 9.0]
    media = calcular_media(notas_exemplo)
    print(f"Média: {media:.1f}")
    print(f"Situação: {situacao_aluno(media)}")
