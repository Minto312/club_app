FROM nginx:latest
RUN rm -f /etc/nginx/conf.d/*
COPY nginx.conf /etc/nginx/conf.d/nginx.conf

COPY club-introduction /var/www/club-introduction
COPY ../../etc /etc

CMD ["nginx","-g","daemon off;","-c","nginx.conf"]