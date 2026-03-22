grammar DevOpsDSL;

// ===============================
// PROGRAMA PRINCIPAL
// ===============================
program: statement* EOF;

// ===============================
// TIPOS DE INSTRUCCIONES
// ===============================
statement : nodeCommand
          | groupCommand
          | deployCommand
          | rule
          | parallelBlock
          ;

// ===============================
// COMANDOS A NODOS
// ===============================
nodeCommand : ID '.' 'run' '(' STRING ')' ;

// ===============================
// COMANDOS A GRUPOS
// ===============================
groupCommand : ID '.' 'update' '(' ')' ;

// ===============================
// DEPLOY
// ===============================
deployCommand : 'deploy' ID 'to' ID ;

// ===============================
// REGLAS (EVENTOS)
// ===============================
rule : condition ARROW action ;

// ===============================
// CONDICIONES
// ===============================
condition : ID '.' ID comparator NUMBER ;
comparator : '>' | '<' | '==' | '!=' | '>=' | '<=';

// ===============================
// ACCIONES
// ===============================
action : ID '(' ')' | ID '.' 'run' '(' STRING ')' ;

// ===============================
// EJECUCIÓN PARALELA
// ===============================
parallelBlock : 'parallel' '{' statement+ '}' ;

// ===============================
// TOKENS
// ===============================
ARROW: '->';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '"' .*? '"';
NUMBER: [0-9]+;

// Ignorar espacios
WS: [ \t\r\n]+ -> skip;
