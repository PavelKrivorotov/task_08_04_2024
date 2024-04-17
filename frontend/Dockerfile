# syntax=docker/dockerfile:1

# vue app
FROM node:20-alpine3.18 AS stage
WORKDIR /app/

COPY ./vite.config.js /app/vite.config.js
COPY ./package.json /app/package.json
# COPY ./package-lock.json /app/package-lock.json
COPY ./jsconfig.json /app/jsconfig.json

RUN npm install

COPY ./index.html /app/index.html
COPY ./public /app/public
COPY ./src /app/src

RUN npm run build


# nginx server
FROM nginx:stable
COPY --from=stage /app/dist /usr/share/nginx/html

EXPOSE 80

# In docker-compose:
#   command: nginx -g 'daemon off;'    (OMG.... fantastic)

CMD [ "nginx", "-g", "daemon off;" ]
