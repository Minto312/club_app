FROM nginx:latest
RUN rm -f /etc/nginx/conf.d/*
COPY nginx.conf /etc/nginx/conf.d/nginx.conf

COPY club-introduction /var/www/club-introduction

# /var/www/etc
COPY ssl /ssl

# RUN mkdir -p /var/log/nginx

CMD ["nginx","-g","daemon off;","-c","nginx.conf"]