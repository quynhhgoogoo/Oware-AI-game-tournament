from envs.state import State


class AgentInterface:
    """
    The interface of an Agent

    This class defines the required methods for an agent class
    """
    @staticmethod
    def info():
        """
        Return the agent's information

        This function returns the agent's information as a dictionary variable.
        The returned dictionary should contain at least the `agent name`.

        Returns
        -------
        Dict[str, str]
        """
        return {"agent name": "mermaid mermaid"}

    def decide(self, state: State, actions: list):
        """
        Generate a sequence of increasing good actions form the `actions` list

        This is a generator function; it means it should have no return
        statement, but it should yield a sequence of increasing good actions.

        Parameters
        ----------
        state: State
            Current state of the game
        actions: list
            List of all possible actions

        Yields
        ------
        action
            the chosen `action` from the `actions` list
        """

        shuffle(actions)
        win_counter = [0] * len(actions)
        counter = 0
        while True:
            counter += 1
            for i, action in enumerate(actions):
                state2 = state.successor(action)
                result = self.__simulator.play(output=False, starting_state=state2)
                win_counter[i] += 1 if result == [state.current_player()] else 0
            yield actions[win_counter.index(max(win_counter))]
