def preguntar_respuesta(pregunta):
    respuesta = input(pregunta + " (s/n): ").strip().lower()
    while respuesta not in ['s', 'n']:
        print("Por favor, responde con 's' para Sí o 'n' para No.")
        respuesta = input(pregunta + " (s/n): ").strip().lower()
    return respuesta == 's'

def evaluar_sintomas():
    print("Por favor, responde las siguientes preguntas con respecto a tus síntomas y antecedentes:")
    viaje_zona_endemica = preguntar_respuesta("¿Has viajado recientemente a una zona endémica del ébola? Cómo en Nzara, Sudán,Yambuku o República Democrática del Congo")
    contacto_enfermo = preguntar_respuesta("¿Has estado en contacto con alguien que ha tenido la enfermedad del ébola?")
    fiebre_alta = preguntar_respuesta("¿Has tenido fiebre alta (39°C) recientemente?")
    dolor_cabeza = preguntar_respuesta("¿Has experimentado dolor de cabeza recientemente?")
    perdida_apetito = preguntar_respuesta("¿Has experimentado pérdida de apetito recientemente?")
    dolor_abdominal = preguntar_respuesta("¿Has tenido dolor abdominal recientemente?")
    dolor_muscular = preguntar_respuesta("¿Has tenido dolor muscular recientemente?")
    cansancio = preguntar_respuesta("¿Te sientes cansado(a) o fatigado(a) últimamente?")
    erupcion_cutanea = preguntar_respuesta("¿Has experimentado erupción cutánea recientemente?")
    vomitos = preguntar_respuesta("¿Has tenido episodios de vómitos recientemente?")
    diarrea = preguntar_respuesta("¿Has tenido diarrea recientemente?")
    nauseas = preguntar_respuesta("¿Has experimentado náuseas recientemente?")
    sangrado_orificios = preguntar_respuesta("¿Has experimentado sangrado por algún orificio del cuerpo?")
    periodo_incubacion = preguntar_respuesta("¿Estás dentro del período de incubación (2 a 21 días) desde la posible exposición al virus?")
    
    sintomas_pesos = [3, 2, 2, 2, 1, 1, 4, 1, 1, 1, 4]  # Pesos asignados a cada síntoma
    factores_pesos = [4, 4, 4]  # Pesos asignados a los factores de riesgo
    
    sintomas = [fiebre_alta, dolor_cabeza, perdida_apetito, dolor_abdominal, dolor_muscular, cansancio, erupcion_cutanea, vomitos, diarrea, nauseas, sangrado_orificios]
    factores = [viaje_zona_endemica, contacto_enfermo, periodo_incubacion]
    
    puntaje_sintomas = sum(peso * int(sintoma) for peso, sintoma in zip(sintomas_pesos, sintomas))
    puntaje_factores = sum(peso * int(factor) for peso, factor in zip(factores_pesos, factores))
    
    puntaje_total = puntaje_sintomas + puntaje_factores
    
    umbral_probabilidad_alta = 15  #puntaje para determinar alta probabilidad
    
    print('')
    if puntaje_total >= umbral_probabilidad_alta:
        print("Basado en tus respuestas, es posible que estés experimentando síntomas relacionados con el ébola.")
        print("Debido a tu exposición a la enfermedad, contacto con personas enfermas, erupción cutánea y período de incubación, se recomienda buscar atención médica de inmediato.")
    else:
        print("Basado en tus respuestas, no parece que estés experimentando síntomas relacionados con el ébola en este momento.")

if __name__ == "__main__":
    evaluar_sintomas()
