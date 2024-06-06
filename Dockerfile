FROM base-cuda-conda

WORKDIR /app
COPY . .

RUN chmod +x /app/setup.sh && /app/setup.sh

# # Info: Points host port 80 to container
# # docker run -p 80:3000 image_id
# # Container must have process running on port 3000 assuming that's how we start.
# EXPOSE 80
# RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/bin/bash", "entrypoint.sh"]