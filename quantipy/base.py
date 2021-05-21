# -*- coding: utf-8 -*-
#https://realpython.com/python-application-layouts/
#https://realpython.com/documenting-python-code/#documenting-your-python-projects
import math            

class Length:
    def __init__(self):
        self._meter = None
        self._foot = None
        
    def __setattr__(self, name, value):
       if name in ['_meter', '_foot', 'm', 'ft', 'km', 'nmi', 'mi', 'inch',
                   'ft_in']:
           object.__setattr__(self, name, value)
       else:
           raise TypeError('Cannot set name %r on object of type %s' % (
                    name, self.__class__.__name__))
    
    def __str__(self):
        return f"{self.m} m"
    
    def __add__(self, other):
        value = self.m + other.m
        retval = Length()
        retval.m = value 
        return retval
    
    def __sub__(self, other):
        value = self.m - other.m
        retval = Length()
        retval.m = value 
        return retval
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            retval = Length()
            retval.m = self.m * other
            return retval
        else:
            raise TypeError('unsupported operand type for *')
    
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            retval = Length()
            retval.m = self.m * other
            return retval
        else:
            raise TypeError('unsupported operand type for *')
        
            
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            retval = Length()
            retval.m = self.m / other
            return retval
        elif isinstance(other, Length):
            return self.m / other.m
        else:
            raise TypeError('unsupported operand type for /')
            
    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            retval = Length()
            retval.m = self.m // other
            return retval
        elif isinstance(other, Length):
            return self.m // other.m
        else:
            raise TypeError('unsupported operand type for /')
        
        
    @property 
    def m(self):
        return self._meter
    
    @m.setter 
    def m(self, value):
        self._meter = float(value)
        self._foot = float(value) / 0.3048
        
    @property 
    def ft(self):
        return self._foot
    
    @ft.setter 
    def ft(self, value):
        self._foot = float(value)
        self._meter = float(value) * 0.3048
        
    @property 
    def km(self):
        return self._meter / 1e3
    
    @km.setter 
    def km(self, value):
        self.m = float(value) * 1e3
        
    @property 
    def nmi(self):
        return self._meter / 1852
    
    @nmi.setter 
    def nmi(self, value):
        self.m = value * 1852
        
    @property 
    def mi(self):
        return self._foot / 5280
    
    @mi.setter 
    def mi(self, value):
        self.ft  = float(value) * 5280
        
    @property
    def inch(self):
        return self._foot * 12
    
    @inch.setter 
    def inch(self, value):
        self.ft = float(value) / 12
        
    @property 
    def ft_in(self):
        ft = math.floor(self._foot)
        inch = (self._foot % ft) * 12
        return (math.floor(self._foot), round(inch, 2))
    
    @ft_in.setter 
    def ft_in(self, values):
        if not len(values) == 2:
            raise ValueError('ft_in requires exactly 2 inputs')
        self.ft = float(values[0]) + float(values[1]) / 12
        
class Mass:
    def __init__(self):
        self._kilogram = None
        self._pound = None
    
    def __setattr__(self, name, value):
       if name in ['_kilogram', '_pound', 'kg', 'lb', 'g', 'oz', 't_uk', 
                   't_us', 't_si']:
           object.__setattr__(self, name, value)
       else:
           raise TypeError('Cannot set name %r on object of type %s' % (
                    name, self.__class__.__name__))
    
    def __str__(self):
        return f"{self.kg} kg"
    
    def __add__(self, other):
        value = self.kg + other.kg
        retval = Mass()
        retval.kg = value 
        return retval
    
    def __sub__(self, other):
        value = self.kg - other.kg
        retval = Mass()
        retval.kg = value 
        return retval
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            retval = Mass()
            retval.kg = self.kg * other
            return retval
        else:
            raise TypeError('unsupported operand type for *')
    
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            retval = Mass()
            retval.kg = self.kg * other
            return retval
        else:
            raise TypeError('unsupported operand type for *')
        
            
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            retval = Mass()
            retval.kg = self.kg / other
            return retval
        elif isinstance(other, Mass):
            return self.kg / other.kg
        else:
            raise TypeError('unsupported operand type for /')
            
    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            retval = Mass()
            retval.kg = self.kg // other
            return retval
        elif isinstance(other, Mass):
            return self.kg // other.kg
        else:
            raise TypeError('unsupported operand type for /')
        
        
    @property 
    def kg(self):
        return self._kilogram
    
    @kg.setter 
    def kg(self, value):
        self._kilogram = float(value)
        self._pound = float(value) / 0.45359237
        
    @property 
    def lb(self):
        return self._pound
    
    @lb.setter 
    def lb(self, value):
        self._pound = float(value)
        self._kilogram = float(value) * 0.45359237
        
    @property 
    def g(self):
        return self._kilogram * 1e3
    
    @g.setter 
    def g(self, value):
        self.kg = float(value) / 1e3
        
    @property 
    def oz(self):
        return self._pound * 16
    
    @oz.setter 
    def oz(self, value):
        self.lb = float(value) / 16
        
    @property 
    def t_uk(self):
        return self._pound / 2240
    
    @t_uk.setter 
    def t_uk(self, value):
        self.lb = value * 2240
        
    @property 
    def t_us(self):
        return self._pound / 2000
    
    @t_us.setter 
    def t_us(self, value):
        self.lb = value * 2000
    
    @property 
    def t_si(self):
        return self._kilogram / 1000
    
    @t_si.setter 
    def t_si(self, value):
        self.kg = value * 1000
        
class Time:
    def __init__(self):
        self._second = None
        
    def __setattr__(self, name, value):
       if name in ['_second', 's', 'ms', 'minutes', 'h', 'hms', 'd']:
           object.__setattr__(self, name, value)
       else:
           raise TypeError('Cannot set name %r on object of type %s' % (
                    name, self.__class__.__name__))
    
    def __add__(self, other):
        value = self.s + other.s
        retval = Time()
        retval.s = value 
        return retval
    
    def __sub__(self, other):
        value = self.s - other.s
        retval = Time()
        retval.s = value 
        return retval
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            retval = Time()
            retval.s = self.s * other
            return retval
        else:
            raise TypeError('unsupported operand type for *')
    
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            retval = Time()
            retval.s = self.s * other
            return retval
        else:
            raise TypeError('unsupported operand type for *')
        
            
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            retval = Time()
            retval.s = self.s / other
            return retval
        elif isinstance(other, Time):
            return self.s / other.s
        else:
            raise TypeError('unsupported operand type for /')
            
    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            retval = Time()
            retval.s = self.s // other
            return retval
        elif isinstance(other, Time):
            return self.s // other.s
        else:
            raise TypeError('unsupported operand type for /')
    
    @property 
    def s(self):
        return self._second
    
    @s.setter 
    def s(self, value):
        self._second = float(value)
        
    @property
    def ms(self):
        return self._second * 1000
    
    @ms.setter
    def ms(self, value):
        self.s = float(value) / 1000
    
    @property
    def minute(self):
        return self._second / 60
    
    @minute.setter
    def minute(self, value):
        self.s = float(value) * 60
        
    @property
    def h(self):
        return self._second / 3600
    
    @h.setter
    def h(self, value):
        self.s = float(value) * 3600
    
    @property
    def d(self):
        return self._second / 86400
    
    @d.setter
    def d(self, value):
        self.s = float(value) * 86400
        
    @property
    def hms(self):
        hour = self._second % 3600
        tmp = self._second - (hour * 3600)
        minute = tmp % 60
        second = tmp - (minute * 60)
        
        return (hour, minute, round(second, 3))
    
    @hms.setter
    def hms(self, values):
        if not len(values) == 3:
            raise ValueError('hms requires 3 exactly inputs')
        self.s = values[0] * 3600 + values[1] * 60 + values[2]
    
        
    
     
        
    
