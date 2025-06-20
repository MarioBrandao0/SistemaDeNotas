# 🎓 Sistema de Notas

> ⚠️ **OBS:** Este projeto está desatualizado. Pode conter funcionalidades inacabadas ou não refletir as melhores práticas atuais.

> ⚠️ **IMPORTANTE:** Este projeto foi desenvolvido apenas para fins educativos e de prática. Não se trata de um sistema profissional ou pronto para uso em ambientes reais.


Sistema simples em Python para registrar notas de alunos, calcular médias e exportar os resultados para uma planilha Excel, separando os alunos por situação (aprovado, recuperação ou reprovado), com coloração indicativa.

---

## 📋 Funcionalidades

- Registro de alunos e suas quatro notas  
- Cálculo automático da média  
- Classificação dos alunos:
  - ✅ Aprovado (nota ≥ 7.0)
  - ⚠️ Recuperação (nota == 6)
  - ❌ Reprovado (nota < 5.0)
- Exportação dos dados para `Alunos.xlsx` com:
  - Abas separadas por situação
  - Células coloridas: verde, amarelo ou vermelho

---

## 🛠️ Tecnologias Utilizadas

- Python 3  
- [pandas](https://pandas.pydata.org/)  
- [openpyxl](https://openpyxl.readthedocs.io/)  

---

## 🚀 Como Executar

```bash
git clone https://github.com/MarioBrandao0/SistemaDeNotas.git
cd SistemaDeNotas
pip install pandas openpyxl
python main.py
```

---

## 🖥️ Exemplo de Uso

```text
1-Registrar nota/2-calcular média/3-Sair: 1
Digite o nome do aluno: João
Digite a nota do aluno[-1 --> Sair]: 6
Digite a nota do aluno[-1 --> Sair]: 7
Digite a nota do aluno[-1 --> Sair]: 5
Digite a nota do aluno[-1 --> Sair]: 8

1-Registrar nota/2-calcular média/3-Sair: 2
[{'Nome': 'João', 'Nota': 6.5}]
Arquivo 'Alunos.xlsx' gerado com sucesso!
```

---

## 📁 Estrutura do Projeto

```plaintext
SistemaDeNotas/
├── main.py
├── funcoes.py
├── Alunos.xlsx
└── README.md
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas!  
Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias ou correções.

---

## 📝 Licença

Este projeto está licenciado sob a licença MIT.

---

## ✨ Autor

**Mario Brandão**  
[https://github.com/MarioBrandao0](https://github.com/MarioBrandao0)
