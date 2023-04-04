FROM node:16

FROM node:16
COPY package*.json ./
RUN npm install
COPY graphqlserver.js ./
EXPOSE 5030
CMD [ "node", "graphqlserver.js" ]