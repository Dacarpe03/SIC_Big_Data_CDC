tweet_tuples = LOAD '/user/student/tweets_preprocessing/*csv' 
  USING PigStorage('\t') 
  AS
  (usuario: chararray,
   mensaje: chararray,
   likes: int);

uniparsed = FOREACH tweet_tuples GENERATE 
  usuario,
  REGEX_EXTRACT(mensaje, '#\\s*(\\w+)', 1),
  mensaje,
  likes;

STORE uniparsed INTO '/user/student/tweets_processed/' USING PigStorage('\t');