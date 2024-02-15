%% Rotina proposta para tratamento de dados do INMET para aplicacao
% Link para os dados: https://portal.inmet.gov.br/dadoshistoricos 
function tbl = dadosINMET(arq)
lastwarn('', '');
opts = delimitedTextImportOptions("NumVariables", 19);

% Specify range and delimiter
opts.DataLines = [10, Inf];
opts.Delimiter = ";";

% Specify column names and types
opts.VariableNames = ["Data", "hora", "precTotal", "patm", "patmMaxAnt", "patmMinAnt", "rad", "tArSeco", "tOrvalhoC", "tmaxNAHORAANTAUTC", "tminNAHORAANTAUTC", "tempOrvMaxAnt", "tempOrvMinAnt", "umidRelMaxAnt", "umidRelMinAnt", "umidRel", "dirVento", "vRajMax", "vHor"];
opts.VariableTypes = ["datetime", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double"];

% Specify file level properties
opts.ExtraColumnsRule = "ignore";
opts.EmptyLineRule = "read";

% Specify variable properties
opts = setvaropts(opts, "Data", "InputFormat", "yyyy/MM/dd");
opts = setvaropts(opts, "hora", "TrimNonNumeric", true);
opts = setvaropts(opts, ["hora", "precTotal", "patm", "patmMaxAnt", "patmMinAnt", "rad", "tArSeco", "tOrvalhoC", "tmaxNAHORAANTAUTC", "tminNAHORAANTAUTC", "tempOrvMaxAnt", "tempOrvMinAnt", "umidRelMaxAnt", "umidRelMinAnt", "umidRel", "dirVento", "vRajMax", "vHor"], "DecimalSeparator", ",");
opts = setvaropts(opts, "hora", "ThousandsSeparator", ".");

% Import the data
tbl = readtable(arq, opts);
[~, warnId] = lastwarn();
if (warnId == "MATLAB:readtable:AllNaTVariable") % possivel erro de formato, tentando com formato antigo
  opts = setvaropts(opts, "Data", "InputFormat", "yyyy-MM-dd");
  tbl = readtable(arq, opts);
  disp('Corrigindo erro de formato...');
end
tbl.Properties.VariableDescriptions = [
  "Data (YYYY/MM/DD)" 
  "Hora UTC" 
  "Precipitacao total horario (mm)" 
  "PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)" 
  "PRESSAO ATMOSFERICA MAX. NA HORA ANT. (AUT) (mB)" 
  "PRESSAO ATMOSFERICA MIN. NA HORA ANT. (AUT) (mB)" 
  "RADIACAO GLOBAL (KJ/m2)" 
  "TEMPERATURA DO AR - BULBO SECO, HORARIA (degC)" 
  "TEMPERATURA DO PONTO DE ORVALHO (degC)" 
  "TEMPERATURA MAX. NA HORA ANT. (AUT) (degC)" 
  "TEMPERATURA MIN. NA HORA ANT. (AUT) (degC)" 
  "TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (degC)" 
  "TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (degC)" 
  "UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)" 
  "UMIDADE REL. MIN. NA HORA ANT. (AUT) (%)" 
  "UMIDADE RELATIVA DO AR, HORARIA (%)" 
  "VENTO, DIRECAO HORARIA (deg)" 
  "VENTO, RAJADA MAXIMA (m/s)" 
  "VENTO, VELOCIDADE HORARIA (m/s)"];
end

