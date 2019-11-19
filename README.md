# esque - an operational Kafka tool

[![pypi Version](https://img.shields.io/pypi/v/esque.svg)](https://pypi.org/project/esque/)
[![Python Versions](https://img.shields.io/pypi/pyversions/esque.svg)](https://pypi.org/project/esque/)
![Build Status](https://github.com/real-digital/esque/workflows/Style,%20Unit%20And%20Integration%20Tests/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/real-digital/esque/badge.svg)](https://coveralls.io/github/real-digital/esque?branch=add-coverage)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

In the Kafka world nothing is easy, but `esque` (pronounced *esk*) is an attempt at it.

`esque` is a user-centric command line interface for Kafka administration. 

## Why should you care?

Some stuff is hard, and that is okay, but listing your kafka topics shouldn't be.

While adopting kafka at real.digital we noticed the immense entry barrier it poses to newcomers. 
We can't recount how often we wrote Slack messages asking for the script to check the 
status of topics or consumer groups. This is partly (but not only) due to a 
fragmented and unclear definition of tooling and APIs for kafka.
In a wide array of administration tools, `esque` distances itself by striving to provide Kafka Ops for Humans, in a usable and natural way.    
  
We feel that the goal of `esque` embodies the principle: “**keep easy things easy, and make hard things possible**”. 

## Principles

* batteries included
* feature rich
* robust
* insightful
* by engineers for engineers

## Feature Overview

* Support for any type of Kafka deployment >1.2
* Display Resources (Topics, Consumer Groups, Brokers)
* Get detailed Overviews of Resources (Topics, Consumer Groups, Brokers)
* Create/Delete Topics
* Edit Topic Configurations
* Edit Consumer Offset for Topics
* SASL/SSL Support out of the box
* Consume and Produce to and from Avro and Plaintext Topics (including Avro Schema Resolution from Schema Registry)
* Context Switch (Easily Switch between pre-defined Clusters)
* Kafka Ping (Test roundtrip time to your kafka cluster)

## Command Overview

```bash
$ esque

Usage: esque [OPTIONS] COMMAND [ARGS]...

  esque - an operational kafka tool.

  In the Kafka world nothing is easy, but esque (pronounced esk) is an
  attempt at it.

Options:
  --recreate-config  Overwrites the config with the sample config.
  --version          Show the version and exit.
  -v, --verbose      Return stack trace on error.
  --no-verify        Skip all verification dialogs and answer them with yes.
  --help             Show this message and exit.

Commands:
  apply     Apply a set of topic configurations.
  config    Configuration-related options.
  consume   Consume messages from a topic.
  create    Create a new instance of a resource.
  ctx       List contexts and switch between them.
  delete    Delete a resource.
  describe  Get detailed information about a resource.
  edit      Edit a resource.
  get       Get a quick overview of different resources.
  ping      Test the connection to the kafka cluster.
  produce   Produce messages to a topic.
  set       Set resource attributes.

```

## Installation and Usage

### Installation

`esque` is available at [pypi.org](https://pypi.org/project/esque/) and can be installed with `pip install esque`. `esque` requires Python 3.6+ to run.

#### SASL Support

When your cluster is secured with SASL authentication, you'll need to install our fork of pykafka since pykafka itself
doesn't support it. We've opened a pull request https://github.com/Parsely/pykafka/pull/972 but at the time of
writing it hasn't been merged yet.

```bash
pip install -U git+https://github.com/real-digital/pykafka.git@feature/sasl-scram-support
```

`esque` will also prompt you with the above command as soon as you need it in case you're not sure if you actually do.

### Autocompletion

The autocompletion scripts for `bash` and `zsh` can be generated by running `esque config autocomplete`.

### Usage

#### Config Definition

When starting `esque` for the first time the following message will appear:

```bash
No config provided in ~/.esque
Should a sample file be created in ~/.esque [y/N]:
```

When answering with `y` `esque` will copy over the [sample config](https://github.com/real-digital/esque/blob/master/esque/config/sample_config.yaml) to `~/.esque/esque_config.yaml`.
Afterwards you can modify that file to fit your cluster definitions.

Alternatively might just provide a config file following the sample config's file in that path.

##### Config Example

```yaml
version: 1
current_context: local
contexts:
  # This context corresponds to a local development cluster
  # created by docker-compose when running esque from the host machine.
  local:
    bootstrap_servers:
      - localhost:9092
    security_protocol: PLAINTEXT
    schema_registry: http://localhost:8081
    default_values:
      num_partitions: 1
      replication_factor: 1
```

#### Config file for "apply" command

The config for the apply command has to be a yaml file and
is given with the option -f or --file.

In the current version only topic configurations can be
changed and specified.

It has to use the same schema, which is used 
for the following example:

```yaml
topics:
  - name: topic_one
    replication_factor: 3
    num_partitions: 50
    config:
      cleanup.policy: compact
  - name: topic_two
    replication_factor: 3
    num_partitions: 50
    config:
      cleanup.policy: compact
```

## Development

To setup your development environment, make sure you have at least Python 3.6 & [poetry](https://github.com/sdispater/poetry) installed, then run 

```bash
poetry install
poetry shell
```

### Pre Commit Hooks

To install pre commit hooks run:

```bash
pip install pre-commit
pre-commit install
pre-commit install-hooks
```

### Run tests

#### Integration Tests

esque comes with a docker-compose based kafka stack which you can start up with `make test-suite`.

You can then run the integration tests against this stack with `pytest tests/ --integration --local`.

Alternatively you can go the fast way and just run the whole stack + integration tests in docker: 

```bash
make integration-test
```

#### Unit Tests

If you only want the unit tests, just run:
 
```bash
make test
```

## Alternatives

- [LinkedIn KafkaTools](https://github.com/linkedin/kafka-tools)
- [PyKafka Tools](https://github.com/Parsely/pykafka/blob/master/pykafka/cli/kafka_tools.py)
- [Official Kafka Scripts](https://github.com/apache/kafka/tree/trunk/bin)
- [kafkacat](https://github.com/edenhill/kafkacat)
