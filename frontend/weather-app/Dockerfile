FROM node:20-alpine

RUN mkdir -p /usr/src/app_fe
WORKDIR /app_fe
ENV PATH="./node_modules/.bin:$PATH"
COPY . /app_fe
RUN npm install --save 
# RUN npm install react-scripts --save
RUN npm run build
# RUN npm start
