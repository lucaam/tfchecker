IMAGE=$(docker build -q .)
docker tag $IMAGE tfchecker:latest
docker run --env-file=.env -it --rm $IMAGE
docker image rm --force $IMAGE