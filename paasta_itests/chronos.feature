Feature: paasta_tools can interact with chronos

  Scenario: Trivial chronos interaction
    Given a working paasta cluster
    When we create a trivial chronos job
    Then we should be able to see it when we list jobs
