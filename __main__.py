import modules.simple_logger as logger

log = logger.LOG(level = 0, filename = "latest.log", filepath = "logs/")

if __name__ == "__main__":
    log.debug("Bot starting...")
    log.save("time")