# coding=utf-8
# The script simulates a streaming socket data source.  It accepts the host and port number of 
# the connection.  It also accepts number of lines to stream per second as well as the name
# of the text to use to simulate the streaming data
#
# Parameters:
#     host: the host name or IP to bind to (e.g. localhost)
#     port: the port to listen on (e.g. 1234)
#
# Note: script makes no attempt to recover from a broken connection; restart the script.

import sys
import time
import socket
import random
import pandas as pd
from faker import Faker


dfUnis = pd.read_csv('../Datos/uni_rankings_final.csv')
listSiglas = dfUnis['siglas']
listUnis = dfUnis['nombre_regional'].apply(str.strip)
universidades = dict()
for i in zip(listUnis, listSiglas):
   universidades[i[0]]=i[1]
universidades

frases = [
"¡La {universidad} me tiene totalmente fascinado! Sus siglos de historia, su arquitectura impresionante y su prestigio académico la convierten en un lugar donde aprender se convierte en una experiencia mágica. {hashtag} #OrgulloUniversitario",

"Estudiar en la {universidad} es un sueño hecho realidad. Sus programas de investigación de vanguardia, el ambiente cosmopolita y el espíritu innovador hacen que cada día sea una oportunidad para crecer y brillar.  {hashtag} #VidaUniversitariaFeliz",

"En la {universidad} no solo encuentro una educación de calidad, sino también un entorno acogedor que fomenta el desarrollo personal. Desde las tapas en el Albaicín hasta las clases en el campus, cada momento es un regalo. {hashtag} #UniversidadDeCercanía",

"La {universidad} es una institución de referencia en el ámbito científico y tecnológico. La pasión de los profesores, los laboratorios de última generación y las oportunidades de colaboración con empresas son un trampolín hacia un futuro brillante. {hashtag} #UniversidadesVanguardistas",

"En la {universidad}, el aprendizaje trasciende las aulas. Sus hermosos jardines, las actividades culturales y el espíritu inclusivo hacen que cada día sea una aventura llena de descubrimientos y crecimiento personal. {hashtag} #UniversidadesSinFronteras",

"La {universidad} es un crisol de cultura, historia y conocimiento. Sus campus vibrantes, la rica vida estudiantil y la calidad educativa la convierten en un lugar excepcional para crecer y desarrollarse. {hashtag} #US {hashtag} #VidaUniversitaria",

"En la {universidad}, cada paso se siente como una peregrinación hacia el conocimiento. Su tradición académica, la belleza de sus edificios históricos y el ambiente intelectual me inspiran cada día. {hashtag} #CaminoDelSabio",

"La {universidad} es un referente en innovación y emprendimiento. Aquí se fomenta el pensamiento crítico, la creatividad y la pasión por el cambio. ¡Preparados para conquistar el futuro! {hashtag} #EspírituEmprendedor",

"Estudiar en la {universidad} es como sumergirse en un oasis de aprendizaje. Su entorno mediterráneo, la calidez de su comunidad estudiantil y las oportunidades de investigación hacen de esta experiencia algo único. {hashtag} #UniversidadEnElParaíso",

"La {universidad}, en las Islas Canarias, combina el encanto de su entorno natural con una educación de calidad. ¡Estudiar aquí es como estar en el paraíso! {hashtag} #EducaciónEnElAtlántico",

"La {universidad} es un lugar donde la tradición se une con la innovación. Sus programas académicos de excelencia y su compromiso con la investigación la convierten en un referente en el mundo académico. {hashtag} #ExcelenciaUniversitaria",

"Estudiar en la {universidad} es un privilegio. Su historia milenaria, sus profesores apasionados y la calidad de su educación me inspiran a dar lo mejor de mí mismo cada día. {hashtag} #PasiónPorElConocimiento",

"La {universidad} es un tesoro académico. Sus campus llenos de historia, su compromiso con la sostenibilidad y el ambiente acogedor hacen que estudiar aquí sea una experiencia inolvidable. {hashtag} #UniversidadSostenible",

"La {universidad} es una joya del Renacimiento. Sus edificios históricos, su atmósfera inspiradora y su comunidad universitaria enérgica la convierten en un lugar único para aprender y crecer. {hashtag} #HerenciaCultural",

"En la {universidad}, el conocimiento se fusiona con la belleza natural de Asturias. Sus programas académicos de excelencia y su espíritu de comunidad hacen que estudiar aquí sea un verdadero privilegio. {hashtag} #ConexiónConLaNaturaleza",

"La {universidad} es un lugar donde la excelencia académica se une con los valores humanos. Su enfoque en la formación integral y la responsabilidad social la convierten en una institución ejemplar. {hashtag} #EducaciónConValores",

"Estudiar en la {universidad} es una experiencia enriquecedora. Sus programas innovadores, la cercanía entre profesores y estudiantes, y la belleza de la región vinícola hacen que la educación sea aún más placentera. {hashtag} #VinoYConocimiento",

"La {universidad} es un espacio de aprendizaje vibrante y diverso. Sus instalaciones modernas, la calidad de sus programas y el ambiente estudiantil amigable la convierten en un lugar ideal para crecer tanto académica como personalmente. {hashtag} #DiversidadUniversitaria",

"En la {universidad}, el aprendizaje se fusiona con el espíritu de aventura. Sus campus enclavados en paradisíacas islas, su enfoque en la investigación y la comunidad estudiantil acogedora la hacen una elección inigualable. {hashtag} #ULPGC {hashtag} #ExperienciaCanaria",

"La {universidad} es una institución que destaca por su compromiso con la sociedad y la excelencia académica. Sus programas interdisciplinarios y su ambiente inclusivo hacen que estudiar aquí sea una oportunidad única de crecimiento personal y profesional. {hashtag} #CompromisoSocial",

"La {universidad} es un centro de conocimiento en constante evolución. Sus programas innovadores, el apoyo a la investigación y el espíritu emprendedor hacen que estudiar aquí sea una experiencia enriquecedora. {hashtag} #InnovaciónUniversitaria",

"En la {universidad}, el aprendizaje va más allá de las aulas. Su ubicación privilegiada, el enfoque en la sostenibilidad y la calidad académica la convierten en un lugar inspirador para formarse como profesional del futuro. {hashtag} #AprendizajeHolístico",

"La {universidad} es un referente en el ámbito científico y tecnológico. Su compromiso con la investigación, el apoyo al emprendimiento y la conexión con la industria hacen que estudiar aquí sea un trampolín hacia el éxito. {hashtag} #CienciaYTecnología",

"La {universidad} es un tesoro académico en pleno corazón de la región. Sus programas de calidad, la riqueza cultural y la calidez de su comunidad estudiantil hacen que cada día sea un nuevo descubrimiento. {hashtag} #ConocimientoEnExtremadura",

"En la {universidad}, el conocimiento se entrelaza con la diversidad cultural. Sus programas bilingües, la calidad de su educación y el ambiente enérgico y multicultural hacen que estudiar aquí sea una experiencia enriquecedora. {hashtag} #DiversidadUniversitaria",

"La {universidad} tiene una gran reputación, pero me decepciona su falta de actualización en los métodos de enseñanza. Esperaba más innovación en el aula. {hashtag} #Desilusión",

"La {universidad} presume de ser inclusiva, pero la falta de apoyo a los estudiantes internacionales es evidente. Necesitan mejorar en brindar recursos y orientación. {hashtag} #EstudiantesInternacionales",

"La {universidad} tiene una belleza arquitectónica impresionante, pero su burocracia y lentitud en los trámites académicos son desesperantes. Esperaba un mejor flujo administrativo. {hashtag} #Ineficiencia",

"La {universidad} es conocida por su enfoque en la tecnología, pero su falta de conexión con la industria y las oportunidades laborales es decepcionante. {hashtag} #DesconexiónLaboral",

"La {universidad} tiene una ubicación privilegiada, pero la falta de inversión en infraestructuras y espacios de estudio es evidente. Necesitan mejorar las instalaciones para los estudiantes. {hashtag} #InfraestructuraDeficiente",

"La {universidad} se jacta de su prestigio, pero la falta de actualización en los planes de estudio y la falta de flexibilidad curricular son decepcionantes. {hashtag} #FaltaDeInnovación",

"La {universidad} presume de ser vanguardista, pero la falta de oportunidades de prácticas profesionales y de conexión con el mundo laboral es preocupante. {hashtag} #DesconexiónProfesional",

"La {universidad} tiene una ubicación privilegiada, pero la falta de inversión en recursos tecnológicos y bibliotecarios limita el acceso a materiales de estudio. {hashtag} #RecursosInsuficientes",

"La {universidad} tiene un entorno natural impresionante, pero la falta de apoyo a proyectos de investigación y la escasez de financiamiento son obstáculos para el desarrollo académico. {hashtag} #FaltaDeApoyo",

"La {universidad} se enorgullece de su compromiso social, pero la falta de diversidad y representación en el cuerpo docente y estudiantil es una preocupación. {hashtag} #FaltaDeDiversidad",

"¡La {universidad} me tiene totalmente decepcionado! Su falta de inversión en infraestructura, su burocracia asfixiante y su ambiente competitivo convierten el aprendizaje en una experiencia desalentadora. {hashtag} #FrustraciónUniversitaria",

"Estudiar en la {universidad} es una pesadilla. Sus programas obsoletos, la falta de diversidad y el conformismo intelectual hacen que cada día sea una lucha por encontrar motivación. {hashtag} #UniversidadSinInspiración",

"En la {universidad} no solo encuentro una educación mediocre, sino también un entorno hostil que frena mi desarrollo personal. Desde el maltrato en el campus hasta las limitadas opciones de ocio, cada momento es una tortura. {hashtag} #UniversidadDeDesconexión",

"La {universidad} es una institución estancada en el pasado, sin visión ni ambición. La falta de apoyo de los profesores, los laboratorios anticuados y las oportunidades limitadas hacen que mi futuro se vea oscuro. {hashtag} #UniversidadesObsoletas",

"En la {universidad}, el aprendizaje se estanca en las aulas. Sus espacios descuidados, la ausencia de actividades culturales y el elitismo excluyente hacen que cada día sea una monotonía sin inspiración. {hashtag} #UniversidadesSinVida",

"¡La {universidad} me tiene completamente desilusionado! Su falta de compromiso con la calidad educativa, su desinterés por la investigación y su ambiente apático convierten el proceso de aprendizaje en una experiencia aburrida y frustrante. {hashtag} #DecepciónUniversitaria",

"Estudiar en la {universidad} es una auténtica pesadilla. Sus programas desactualizados, la falta de recursos y la incompetencia de algunos profesores hacen que cada día sea un desafío insoportable. {hashtag} #UniversidadSinProgreso",

"En la {universidad} no solo encuentro una educación deficiente, sino también un entorno tóxico que dificulta mi desarrollo personal. Desde la competencia desmedida hasta el elitismo despreciable, cada momento se convierte en una batalla emocional. {hashtag} #UniversidadDeDestrucción",

"La {universidad} es una institución anclada en el pasado, sin adaptación a los avances tecnológicos ni visión de futuro. La falta de inversión en laboratorios, la burocracia ineficiente y las oportunidades limitadas son una barrera insalvable hacia el éxito. {hashtag} #UniversidadesEstancadas",

"En la {universidad}, el aprendizaje se estanca y la creatividad muere. Sus espacios desmotivadores, la ausencia de eventos enriquecedores y la falta de apoyo académico convierten cada día en una batalla contra la mediocridad. {hashtag} #UniversidadesSinInspiración",

"¡La {universidad} me tiene completamente frustrado! Su falta de recursos actualizados, su desorganización administrativa y su enfoque teórico sin aplicación práctica convierten el proceso de aprendizaje en una pérdida de tiempo y energía. {hashtag} #FrustraciónUniversitaria",

"Estudiar en la {universidad} es un auténtico calvario. Sus programas académicos desactualizados, la falta de conexión con el mundo laboral y la ausencia de oportunidades de crecimiento hacen que cada día sea una batalla cuesta arriba. {hashtag} #UniversidadSinPerspectivas",

"En la {universidad} no solo encuentro una educación deficiente, sino también un entorno competitivo y alienante que dificulta cualquier intento de colaboración. Desde las tensiones constantes hasta la falta de apoyo emocional, cada momento es una lucha solitaria. {hashtag} #UniversidadDeDesconexión",

"La {universidad} es una institución que se queda rezagada en el tiempo, sin adaptarse a las demandas y avances del mundo moderno. La falta de tecnología, la carencia de programas actualizados y las oportunidades limitadas reflejan su falta de relevancia. {hashtag} #UniversidadesObsoletas",

"En la {universidad}, el aprendizaje se ve asfixiado por la monotonía y la falta de inspiración. Sus espacios grises y descuidados, la ausencia de eventos culturales y el conformismo académico convierten cada día en una repetición sin sentido. {hashtag} #UniversidadesSinVida",

"¡La {universidad} me tiene completamente desencantado! Su falta de liderazgo académico, su ambiente opresivo y su enfoque obsoleto convierten el proceso educativo en una experiencia desalentadora y sin valor. {hashtag} #DesilusiónUniversitaria",

"Estudiar en la {universidad} es una auténtica pesadilla. Sus programas desactualizados, la incompetencia de algunos profesores y la ausencia de innovación hacen que cada día sea un desperdicio de tiempo y esfuerzo. {hashtag} #UniversidadSinProgreso",

"En la {universidad} no solo encuentro una educación deficiente, sino también un entorno lleno de discriminación y elitismo. Desde la falta de diversidad hasta la falta de apoyo a los estudiantes, cada momento es una lucha por encontrar un sentido de pertenencia. {hashtag} #UniversidadDeExclusión",

"La {universidad} es una institución estancada en el pasado, sin adaptación a los cambios sociales y tecnológicos. La falta de inversión en recursos, los planes de estudio desactualizados y la burocracia asfixiante son un obstáculo insuperable para el desarrollo personal. {hashtag} #UniversidadesEstancadas",

"En la {universidad}, el aprendizaje se ve sofocado por la falta de motivación y la ausencia de desafíos intelectuales. Sus espacios grises y deprimentes, la escasez de actividades extracurriculares y el desinterés de los profesores convierten cada día en una rutina sin inspiración. {hashtag} #UniversidadesSinEstímulo",

"¡La {universidad} me tiene completamente indignado! Su falta de transparencia, su corrupción interna y su negligencia académica convierten el proceso educativo en una farsa indignante y deshonesta. {hashtag} #IndignaciónUniversitaria",

"Estudiar en la {universidad} es una verdadera tortura. Sus programas desfasados, la incompetencia y desinterés de los profesores, y el ambiente de favoritismo hacen que cada día sea una batalla contra la mediocridad. {hashtag} #UniversidadSinCalidad",

"En la {universidad} no solo encuentro una educación deficiente, sino también un entorno tóxico y deshumanizante. Desde el acoso entre estudiantes hasta la falta de apoyo emocional, cada momento es una lucha por mantener la cordura. {hashtag} #UniversidadDeMalestar",

"La {universidad} es una institución que carece de ética y valores. La falta de integridad académica, los escándalos de corrupción y la impunidad reinante son un golpe a la confianza y la honestidad. {hashtag} #UniversidadesCorruptas",

"En la {universidad}, el aprendizaje se ve frustrado por la falta de recursos y la negligencia institucional. Sus instalaciones deplorables, la escasez de oportunidades de investigación y la falta de compromiso académico convierten cada día en una pérdida de tiempo. {hashtag} #UniversidadesIneficientes",

"¡La {universidad} me tiene completamente desanimado! Su falta de apoyo a los estudiantes, su ambiente competitivo y su enfoque teórico sin aplicación práctica convierten el proceso educativo en una experiencia desmotivante y desesperanzadora. {hashtag} #DesánimoUniversitario",

"Estudiar en la {universidad} es como caminar por un desierto sin oasis. Sus programas académicos desactualizados, la ausencia de mentores inspiradores y la falta de oportunidades reales de crecimiento hacen que cada día sea una batalla contra la apatía. {hashtag} #UniversidadSinMotivación",

"En la {universidad} no solo encuentro una educación deficiente, sino también un entorno alienante y solitario. Desde la falta de compañerismo hasta la falta de apoyo emocional, cada momento se convierte en un recordatorio doloroso de la desconexión. {hashtag} #UniversidadDeSoledad",

"La {universidad} es una institución que ha perdido su rumbo. La falta de visión de futuro, la falta de inversión en infraestructura y la escasez de programas actualizados reflejan una falta de compromiso con la excelencia educativa. {hashtag} #UniversidadesDesorientadas",

"En la {universidad}, el aprendizaje se ve ahogado por la monotonía y la falta de inspiración. Sus espacios grises y desprovistos de vida, la escasa interacción con profesionales del campo y el conformismo académico convierten cada día en una lucha contra el estancamiento. {hashtag} #UniversidadesSinPasión",

"¡La {universidad} me tiene completamente frustrado y enfurecido! Su falta de atención a las necesidades de los estudiantes, su negligencia en resolver problemas y su indiferencia hacia los reclamos legítimos convierten el proceso educativo en una batalla agotadora e injusta. {hashtag} #FrustraciónUniversitaria",

"Estudiar en la {universidad} es una verdadera pesadilla. Sus programas desorganizados, la falta de apoyo docente y la falta de oportunidades de desarrollo profesional hacen que cada día sea una lucha constante por obtener una educación de calidad. {hashtag} #UniversidadSinCompromiso",

"En la {universidad} no solo encuentro una educación deficiente, sino también un entorno de discriminación y desigualdad. Desde la falta de inclusión hasta la falta de diversidad en el cuerpo estudiantil, cada momento es una herida abierta en la búsqueda de equidad. {hashtag} #UniversidadDeInjusticia",

"La {universidad} es una institución que se ha vuelto completamente ajena a las necesidades del mundo actual. La falta de actualización curricular, la resistencia al cambio y la falta de conexión con la realidad laboral son un obstáculo insalvable para el éxito profesional. {hashtag} #UniversidadesDesconectadas",

"En la {universidad}, el aprendizaje se ve sofocado por la falta de recursos y la incompetencia administrativa. Sus instalaciones deterioradas, la escasez de materiales y la falta de oportunidades de investigación limitan seriamente el desarrollo académico. {hashtag} #UniversidadesSinRecursos",

"¡La {universidad} me tiene completamente desilusionado y desesperanzado! Su falta de compromiso con la calidad educativa, su desprecio por la diversidad y su enfoque anticuado convierten el proceso de aprendizaje en una experiencia desalentadora y sin sentido. {hashtag} #DesilusiónUniversitaria",

"Estudiar en la {universidad} es como caminar en círculos sin llegar a ninguna parte. Sus programas desactualizados, la falta de innovación pedagógica y la ausencia de enfoque práctico hacen que cada día sea una lucha por encontrar relevancia y aplicabilidad. {hashtag} #UniversidadSinPropósito",

"En la {universidad} no solo encuentro una educación deficiente, sino también un entorno hostil y segregado. Desde la falta de inclusión hasta la discriminación sistemática, cada momento se convierte en una batalla contra la desigualdad y la exclusión. {hashtag} #UniversidadDeInjusticia",

"La {universidad} es una institución que ha perdido su brillo. La falta de inversión en investigación, la carencia de profesores motivados y la ausencia de colaboraciones con la industria reflejan una falta de compromiso con la excelencia académica. {hashtag} #UniversidadesEstancadas",

"En la {universidad}, el aprendizaje se ve sofocado por la rutina y la falta de inspiración. Sus espacios monótonos y desprovistos de vida, la ausencia de eventos culturales y la falta de estímulo intelectual convierten cada día en una lucha contra la apatía. {hashtag} #UniversidadesSinPasión"]


def generar_tweet_falso(faker):
    usuario = faker.user_name()
    likes = random.randint(0, 1000)
    uni = random.choice(list(universidades.keys()))
    mensaje = random.choice(frases).replace("{universidad}", uni).replace("{hashtag}", '#'+universidades.get(uni))

    return {'usuario': usuario, 'mensaje': mensaje, 'likes': likes}
  
if __name__ == "__main__":
  
  # The host to connect to
  host = sys.argv[1]
  
  # The port to send
  port = int(sys.argv[2])
  
  # Time between sending
  sleeptime = 2 
  
  print(f"Creating socket for host:{host}:{port}")
  # Create socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((host,port))
  print("Socket created sucessfully")
  
  # Instantiate faker to create fake usernames
  faker = Faker()
  
  # Loop to send tweets
  while(1):
    # Generate a fake tweet
    print("Generating fake tweet:")
    tweet = generar_tweet_falso(faker)
    print(tweet)
    # Parse the tweet
    msg = f"{tweet['usuario']}	{tweet['mensaje']}	{tweet['likes']}\n"
    # Send the tweet
    print("Sending tweet")
    s.send(msg.encode('utf-8'))
    print("Tweet sent correctly")
    print("Waiting for more tweets...")
    time.sleep(sleeptime)
