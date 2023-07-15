import random
from faker import Faker
import csv
import pandas as pd

faker = Faker()

universidades = ['Universidad Complutense de Madrid',
    'Universidad de Barcelona',
    'Universidad Autónoma de Madrid',
    'Universidad de Valencia',
    'Universidad de Sevilla',
    'Universidad de Granada',
    'Universitat Pompeu Fabra',
    'Universidad de Salamanca',
    'Universidad de Zaragoza',
    'Universidad de Málaga',
    'Universidad de Santiago de Compostela',
    'Universidad de Valladolid',
    'Universitat de les Illes Balears',
    'Universidad de Córdoba',
    'Universidad Politécnica de Madrid',
    'Universidad de Alicante',
    'Universidad de La Laguna',
    'Universidad de Oviedo',
    'Universidad de Alcalá',
    'Universitat de Girona',
    'Universidad de Murcia',
    'Universidad de Navarra',
    'Universidad de Castilla-La Mancha',
    'Universitat Rovira i Virgili',
    'Universidad de Extremadura',
    'Universidad de Jaén',
    'Universidad de Las Palmas de Gran Canaria',
    'Universitat de Lleida',
    'Universidad de La Rioja',
    'Universidad de Cantabria']

frases = [
  "¡La Universidad de Salamanca me tiene totalmente fascinado! Sus siglos de historia, su arquitectura impresionante y su prestigio académico la convierten en un lugar donde aprender se convierte en una experiencia mágica. #MagiaEnSalamanca #OrgulloUniversitario",

"Estudiar en la Universidad Autónoma de Barcelona es un sueño hecho realidad. Sus programas de investigación de vanguardia, el ambiente cosmopolita y el espíritu innovador hacen que cada día sea una oportunidad para crecer y brillar. #UABarcelona #VidaUniversitariaFeliz",

"En la Universidad de Granada no solo encuentro una educación de calidad, sino también un entorno acogedor que fomenta el desarrollo personal. Desde las tapas en el Albaicín hasta las clases en el campus, cada momento es un regalo. #UGR #UniversidadDeCercanía",

"La Politécnica de Madrid es una institución de referencia en el ámbito científico y tecnológico. La pasión de los profesores, los laboratorios de última generación y las oportunidades de colaboración con empresas son un trampolín hacia un futuro brillante. #UPM #UniversidadesVanguardistas",

"En la Universidad de Valencia, el aprendizaje trasciende las aulas. Sus hermosos jardines, las actividades culturales y el espíritu inclusivo hacen que cada día sea una aventura llena de descubrimientos y crecimiento personal. #UV #UniversidadesSinFronteras",

"La Universidad de Sevilla es un crisol de cultura, historia y conocimiento. Sus campus vibrantes, la rica vida estudiantil y la calidad educativa la convierten en un lugar excepcional para crecer y desarrollarse. #US #VidaUniversitaria",

"En la Universidad de Santiago de Compostela, cada paso se siente como una peregrinación hacia el conocimiento. Su tradición académica, la belleza de sus edificios históricos y el ambiente intelectual me inspiran cada día. #USC #CaminoDelSabio",

"La Universidad Carlos III de Madrid es un referente en innovación y emprendimiento. Aquí se fomenta el pensamiento crítico, la creatividad y la pasión por el cambio. ¡Preparados para conquistar el futuro! #UC3M #EspírituEmprendedor",

"Estudiar en la Universidad de Málaga es como sumergirse en un oasis de aprendizaje. Su entorno mediterráneo, la calidez de su comunidad estudiantil y las oportunidades de investigación hacen de esta experiencia algo único. #UMA #UniversidadEnElParaíso",

"La Universidad de La Laguna, en las Islas Canarias, combina el encanto de su entorno natural con una educación de calidad. ¡Estudiar aquí es como estar en el paraíso! #ULL #EducaciónEnElAtlántico",

"La Universidad de Zaragoza es un lugar donde la tradición se une con la innovación. Sus programas académicos de excelencia y su compromiso con la investigación la convierten en un referente en el mundo académico. #Unizar #ExcelenciaUniversitaria",

"Estudiar en la Universidad de Valladolid es un privilegio. Su historia milenaria, sus profesores apasionados y la calidad de su educación me inspiran a dar lo mejor de mí mismo cada día. #UVa #PasiónPorElConocimiento",

"La Universidad de Córdoba es un tesoro académico. Sus campus llenos de historia, su compromiso con la sostenibilidad y el ambiente acogedor hacen que estudiar aquí sea una experiencia inolvidable. #UCO #UniversidadSostenible",

"La Universidad de Alcalá es una joya del Renacimiento. Sus edificios históricos, su atmósfera inspiradora y su comunidad universitaria enérgica la convierten en un lugar único para aprender y crecer. #UAH #HerenciaCultural",

"En la Universidad de Oviedo, el conocimiento se fusiona con la belleza natural de Asturias. Sus programas académicos de excelencia y su espíritu de comunidad hacen que estudiar aquí sea un verdadero privilegio. #UniOvi #ConexiónConLaNaturaleza",

"La Universidad de Deusto es un lugar donde la excelencia académica se une con los valores humanos. Su enfoque en la formación integral y la responsabilidad social la convierten en una institución ejemplar. #Deusto #EducaciónConValores",

"Estudiar en la Universidad de La Rioja es una experiencia enriquecedora. Sus programas innovadores, la cercanía entre profesores y estudiantes, y la belleza de la región vinícola hacen que la educación sea aún más placentera. #UR #VinoYConocimiento",

"La Universidad de Murcia es un espacio de aprendizaje vibrante y diverso. Sus instalaciones modernas, la calidad de sus programas y el ambiente estudiantil amigable la convierten en un lugar ideal para crecer tanto académica como personalmente. #UMU #DiversidadUniversitaria",

"En la Universidad de Las Palmas de Gran Canaria, el aprendizaje se fusiona con el espíritu de aventura. Sus campus enclavados en paradisíacas islas, su enfoque en la investigación y la comunidad estudiantil acogedora la hacen una elección inigualable. #ULPGC #ExperienciaCanaria",

"La Universidad Pública de Navarra es una institución que destaca por su compromiso con la sociedad y la excelencia académica. Sus programas interdisciplinarios y su ambiente inclusivo hacen que estudiar aquí sea una oportunidad única de crecimiento personal y profesional. #UPNA #CompromisoSocial",

"La Universidad Rey Juan Carlos es un centro de conocimiento en constante evolución. Sus programas innovadores, el apoyo a la investigación y el espíritu emprendedor hacen que estudiar aquí sea una experiencia enriquecedora. #URJC #InnovaciónUniversitaria",

"En la Universidad de Cantabria, el aprendizaje va más allá de las aulas. Su ubicación privilegiada, el enfoque en la sostenibilidad y la calidad académica la convierten en un lugar inspirador para formarse como profesional del futuro. #UC #AprendizajeHolístico",

"La Universidad Jaume I es un referente en el ámbito científico y tecnológico. Su compromiso con la investigación, el apoyo al emprendimiento y la conexión con la industria hacen que estudiar aquí sea un trampolín hacia el éxito. #UJI #CienciaYTecnología",

"La Universidad de Extremadura es un tesoro académico en pleno corazón de la región. Sus programas de calidad, la riqueza cultural y la calidez de su comunidad estudiantil hacen que cada día sea un nuevo descubrimiento. #UEx #ConocimientoEnExtremadura",

"En la Universidad del País Vasco, el conocimiento se entrelaza con la diversidad cultural. Sus programas bilingües, la calidad de su educación y el ambiente enérgico y multicultural hacen que estudiar aquí sea una experiencia enriquecedora. #UPV #DiversidadUniversitaria",

"La Universidad de Salamanca tiene una gran reputación, pero me decepciona su falta de actualización en los métodos de enseñanza. Esperaba más innovación en el aula. #UniversidadDeSalamanca #Desilusión",

"La Universidad Autónoma de Barcelona presume de ser inclusiva, pero la falta de apoyo a los estudiantes internacionales es evidente. Necesitan mejorar en brindar recursos y orientación. #UABarcelona #EstudiantesInternacionales",

"La Universidad de Granada tiene una belleza arquitectónica impresionante, pero su burocracia y lentitud en los trámites académicos son desesperantes. Esperaba un mejor flujo administrativo. #UniversidadDeGranada #Ineficiencia",

"La Politécnica de Madrid es conocida por su enfoque en la tecnología, pero su falta de conexión con la industria y las oportunidades laborales es decepcionante. #UPM #DesconexiónLaboral",

"La Universidad de Valencia tiene una ubicación privilegiada, pero la falta de inversión en infraestructuras y espacios de estudio es evidente. Necesitan mejorar las instalaciones para los estudiantes. #UV #InfraestructuraDeficiente",

"La Universidad de Sevilla se jacta de su prestigio, pero la falta de actualización en los planes de estudio y la falta de flexibilidad curricular son decepcionantes. #UniversidadDeSevilla #FaltaDeInnovación",

"La Universidad Carlos III de Madrid presume de ser vanguardista, pero la falta de oportunidades de prácticas profesionales y de conexión con el mundo laboral es preocupante. #UC3M #DesconexiónProfesional",

"La Universidad de Málaga tiene una ubicación privilegiada, pero la falta de inversión en recursos tecnológicos y bibliotecarios limita el acceso a materiales de estudio. #UMA #RecursosInsuficientes",

"La Universidad de La Laguna tiene un entorno natural impresionante, pero la falta de apoyo a proyectos de investigación y la escasez de financiamiento son obstáculos para el desarrollo académico. #ULL #FaltaDeApoyo",

"La Universidad Pública de Navarra se enorgullece de su compromiso social, pero la falta de diversidad y representación en el cuerpo docente y estudiantil es una preocupación. #UPNA #FaltaDeDiversidad"
]


    
def generar_tweet_falso():
    usuario = faker.user_name()
    likes = random.randint(0, 1000)
    mensaje = random.choice(frases)

    return {'usuario': usuario, 'mensaje': mensaje, 'likes': likes}

# Generar 100 tweets falsos sobre universidades españolas con usuarios y frases aleatorias en español
tweets = []
for _ in range(100):
    tweet = generar_tweet_falso()
    tweets.append(tweet)
    print(tweet)
    print('---')

# Guardar los tweets en un archivo CSV
filename = 'tweets.csv'
df = pd.DataFrame(tweets)
df.to_csv(filename, index=False, encoding='utf-8')
print(f'Tweets guardados en el archivo: {filename}')