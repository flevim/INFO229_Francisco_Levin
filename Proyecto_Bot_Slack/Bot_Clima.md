# Bot Slack del clima

Arquitectura de Bot de **Slack** implementado en Python/Docker/RabbitMQ interactuando con la API gratuita [OpenWheater](https://openweathermap.org/api) para consultar datos del clima de distintas cuidades del mundo, entregando el pronóstico para tres días con información de utilidad. 

Integrantes:
- Francisco Levin
- Diego Mora

Antes de ejecutar *docker-compose* es necesario agregar en `bot_slack_writer/Dockerfile` y `bot_slack_reader/Dockerfile`
las siguientes api keys de Slack

- Bot User OAuth Access Token
- Signing Secret

Tambien es necesario modificar el canal de Slack personal para probar el bot. Para modificarlo se debe editar 
`bot_slack_writer/nestor_slack_writer.py`


