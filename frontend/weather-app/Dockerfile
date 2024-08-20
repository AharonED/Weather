FROM node:15.13-alpine

RUN mkdir -p /usr/src/app_fe
WORKDIR /app_fe
ENV PATH="./node_modules/.bin:$PATH"
COPY . /app_fe
RUN npm install -g --save 
RUN npm install react-scripts --save
RUN npm run build
# RUN npm start
