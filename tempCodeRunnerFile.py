 Increment the counter for the item and update the counter label
    item_counters[name].config(text=str(int(item_counters[name].cget("text")) + 1))