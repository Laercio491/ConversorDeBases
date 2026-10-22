
from flask import Flask, render_template, request

app = Flask(__name__)


def decimal_para_base(numero, base):
    digitos = "0123456789ABCDEF"

    if numero == 0:
        return "0"

    resultado = ""

    while numero > 0:
        resto = numero % base
        resultado = digitos[resto] + resultado
        numero //= base

    return resultado


def base_para_decimal(numero, base):
    digitos = "0123456789ABCDEF"
    numero = numero.upper()
    resultado = 0

    for caractere in numero:
        valor = digitos.index(caractere)
        resultado = resultado * base + valor

    return resultado

def hexadecimal_para_binario(numero, base):
    digitos = "0123456789ABCDEF"
    numero = numero.upper()
    resultado = ""
    
    for caractere in numero:
        if caractere =='0':
            resultado+='0000'
        if caractere == '1':
            resultado+='0001'
        if caractere == '2':
            resultado+='0010'
        if caractere == '3':
            resultado+='0011'
        if caractere == '4':
            resultado+='0100'
        if caractere == '5':
            resultado+='0101'
        if caractere == '6':
            resultado+='0110'
        if caractere == '7':
            resultado+='0111'
        if caractere == '8':
            resultado+='1000'
        if caractere == '9':
            resultado+='1001'
        if caractere == 'A':
            resultado+='1010'    
        if caractere == 'B':
            resultado+='1011'
        if caractere == 'C':
            resultado+='1100'
        if caractere == 'D':
            resultado+='1101'
        if caractere == 'E':
            resultado+='1110'
        if caractere == 'F':
            resultado+='1111'
        else:
            return 
    
    return resultado



@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/integrantes")
def integrantes():
    return render_template("integrantes.html")


@app.route("/conversor", methods=["GET", "POST"])
def conversor():
    decimal = ""
    binario = ""
    hexadecimal = ""

    decimal_binario = ""
    decimal_hexadecimal = ""
    decimal_octal = ""

    binario_decimal = ""
    binario_hexadecimal = ""
    binario_octal = ""

    hexa_decimal = ""
    hexa_binario = ""
    hexa_octal = ""

    erro_decimal = ""
    erro_binario = ""

    if request.method == "POST":
        tipo = request.form.get("tipo")

        if tipo == "decimal":
            decimal = request.form.get("decimal", "").strip()

            try:
                if not decimal or not decimal.isdigit():
                    raise ValueError

                numero = int(decimal)

                decimal_binario = decimal_para_base(numero, 2)
                decimal_hexadecimal = decimal_para_base(numero, 16)
                decimal_octal = decimal_para_base(numero, 8)

            except ValueError:
                erro_decimal = "Digite um número decimal inteiro válido."

        elif tipo == "binario":
            binario = request.form.get("binario", "").strip()

            try:
                if not binario or any(digito not in "01" for digito in binario):
                    raise ValueError

                numero = base_para_decimal(binario, 2)

                binario_decimal = str(numero)
                binario_hexadecimal = decimal_para_base(numero, 16)
                binario_octal = decimal_para_base(numero, 8)

            except ValueError:
                erro_binario = "Digite somente 0 e 1."


    return render_template(
        "conversor.html",
        decimal=decimal,
        binario=binario,
        hexadecimal=hexadecimal,
        decimal_binario=decimal_binario,
        decimal_hexadecimal=decimal_hexadecimal,
        decimal_octal=decimal_octal,
        binario_decimal=binario_decimal,
        binario_hexadecimal=binario_hexadecimal,
        binario_octal=binario_octal,
        erro_decimal=erro_decimal,
        erro_binario=erro_binario
    )


if __name__ == "__main__":
    app.run(debug=True)
