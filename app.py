
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
    octal = ""

    decimal_binario = ""
    decimal_hexadecimal = ""
    decimal_octal = ""

    binario_decimal = ""
    binario_hexadecimal = ""
    binario_octal = ""

    hexadecimal_decimal = ""
    hexadecimal_binario = ""
    hexadecimal_octal = ""

    octal_decimal = ""
    octal_binario = ""
    octal_hexadecimal = ""

    erro_decimal = ""
    erro_binario = ""
    erro_hexadecimal = ""
    erro_octal = ""

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

        elif tipo == "hexadecimal":
            hexadecimal = request.form.get("hexadecimal", "").strip()
                
            try:
                    digitos_validos = "0123456789ABCDEF"

                    if not hexadecimal or any(
                        digito.upper() not in digitos_validos
                        for digito in hexadecimal
                    ):
                        raise ValueError
                
                    numero = base_para_decimal(hexadecimal, 16)
                
                    
                    hexadecimal_binario = decimal_para_base(numero, 2)
                    hexadecimal_decimal = str(numero)
                    hexadecimal_octal = decimal_para_base(numero, 8)
                
            except ValueError:
                    erro_hexadecimal = "Digite somente valores hexadecimais válidos."

        elif tipo == "octal":
                    octal = request.form.get("octal", "").strip()
                        
                    try:
                            digitos_validos = "01234567"
        
                            if not octal or any(
                                digito.upper() not in digitos_validos
                                for digito in octal
                            ):
                                raise ValueError
                        
                            numero = base_para_decimal(octal, 8)
                        
                            
                            octal_binario = decimal_para_base(numero, 2)
                            octal_decimal = str(numero)
                            octal_hexadecimal = decimal_para_base(numero, 16)
                        
                    except ValueError:
                            erro_octal = "Digite somente valores octais válidos."
              
                


    return render_template(
        "conversor.html",
        decimal=decimal,
        binario=binario,
        hexadecimal=hexadecimal,
        octal=octal,
        decimal_binario=decimal_binario,
        decimal_hexadecimal=decimal_hexadecimal,
        decimal_octal=decimal_octal,
        binario_decimal=binario_decimal,
        binario_hexadecimal=binario_hexadecimal,
        binario_octal=binario_octal,
        hexadecimal_binario=hexadecimal_binario,
        hexadecimal_decimal=hexadecimal_decimal,
        hexadecimal_octal=hexadecimal_octal,
        octal_decimal=octal_decimal,
        octal_binario=octal_binario,
        octal_hexadecimal=octal_hexadecimal,
        erro_decimal=erro_decimal,
        erro_binario=erro_binario,
        erro_hexadecimal=erro_hexadecimal,
        erro_octal=erro_octal
    )


if __name__ == "__main__":
    app.run(debug=True)
