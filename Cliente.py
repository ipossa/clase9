class cliente:
    def __init__(self,nombreCompleto,
                 usuario,
                 contraseña,
                 contraseña2,
                 documento,
                 correo,
                 Pregunta1,
                 respuesta1,
                 Pregunta2,
                 respuesta2,
                 Pregunta3,
                 respuesta3,
                 ):
        self.nombreCompleto = nombreCompleto

        self.usuario = usuario
        self.contraseña = contraseña
        self.contraseña2 = contraseña2
        self.documento = documento
        self.correo = correo
        self.Pregunta1 = Pregunta1
        self.respuesta1 = respuesta1
        self.Pregunta2 = Pregunta2
        self.respuesta2 = respuesta2
        self.Pregunta3 = Pregunta3
        self.respuesta3 = respuesta3

    def __str__(self):
        return f"Nombre:{self.nombreCompleto} documento: {self.documento}"




