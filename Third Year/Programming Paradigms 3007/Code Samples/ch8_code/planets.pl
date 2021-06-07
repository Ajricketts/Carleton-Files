star(sol).
orbits(mercury,sol).
orbits(venus,sol).
orbits(earth,sol).
orbits(mars,sol).
orbits(jupiter, sol).
orbits(saturn,sol).
orbits(uranus,sol).
orbits(neptune,sol).
orbits(pluto,sol).
orbits(luna,earth).
orbits(phobos,mars).
orbits(deimos,mars).
orbits(ganymede, jupiter).
orbits(callisto,jupiter).
orbits(io,jupiter).
orbits(europa,jupiter).
orbits(titan,saturn).
orbits(rhea,saturn).
orbits(iapetus,saturn).
orbits(dione,saturn).
orbits(titania, uranus).
orbits(oberon,uranus).
orbits(umbriel, uranus).
orbits(ariel, uranus).
orbits(triton,neptune).
orbits(proteus,neptune).
orbits(charon,pluto).

is_satellite(S):- orbits(S,_).
planet(P):- orbits(P,S),star(S).
moon(M,P):- orbits(M,P),planet(P).
is_moon(M):- orbits(M,P),planet(P).
is_moon(M):- moon(M,_).




