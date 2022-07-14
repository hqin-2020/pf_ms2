
def particle_append(Input):
    θ_coll, i = Input
    θ_t = [i]
    for θs in θ_coll:
        θ_t = θ_t + θs[i]
    return θ_t