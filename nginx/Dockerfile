FROM nginx:latest
RUN rm -f /etc/nginx/conf.d/*
COPY nginx.conf /etc/nginx/conf.d/nginx.conf
# COPY ./nginx/static/ /app/static/

# COPY entrypoint.sh /var/tmp/
# CMD bash /var/tmp/entrypoint.sh


CMD ["nginx","-g","daemon off;","-c","nginx.conf"]