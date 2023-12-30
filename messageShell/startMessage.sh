#!/bin/bash

GREEN="\033[0;32m"
LIGHTBLUE="\33[0;34m"
YELLOW="\33[1;33m"
NC="\033[0m"
echo ""
printf "✅ Container v-league-data_selenium_1  ${GREEN}Started${NC}\n✅ Container v-league-data_python_1  ${GREEN}Started${NC}\n"
echo ""
printf "Point your WebDriver tests to ${LIGHTBLUE}http://localhost:4444${NC}\n"
printf "👀 To see what is happening inside the container, head to ${LIGHTBLUE}http://localhost:7900/?autoconnect=1&resize=scale&password=secret${NC}.\n"
echo ""
printf "${YELLOW}Next command:${NC} make enter\n"
echo ""