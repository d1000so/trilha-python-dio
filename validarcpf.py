import re

class ValidarCPF:
    @staticmethod
    def validar_cpf(cpf):
        # Remover caracteres não numéricos
        cpf_numerico = re.sub(r'[^0-9]', '', cpf)

        # Verificar se o CPF tem 11 dígitos
        if len(cpf_numerico) != 11:
            return False

        # Calcular os dígitos verificadores
        cpf_sem_dv = [int(digito) for digito in cpf_numerico[:-2]]
        dv1 = ValidarCPF.calcular_digito_verificador(cpf_sem_dv)
        dv2 = ValidarCPF.calcular_digito_verificador(cpf_sem_dv + [dv1])

        # Verificar se os dígitos verificadores são iguais aos fornecidos
        return cpf_numerico[-2:] == f"{dv1}{dv2}"

    @staticmethod
    def calcular_digito_verificador(cpf_sem_dv):
        total = 0
        peso = len(cpf_sem_dv) + 1

        for digito in cpf_sem_dv:
            total += int(digito) * peso
            peso -= 1

        resto = total % 11

        if resto < 2:
            return 0
        else:
            return 11 - resto
