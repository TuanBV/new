var schema = {
  type: "object",
  properties: {
    fullname: {
      type: "string",
      minLength: 1,
      maxLength: 200,
    },
    username: { 
      type: "date"
    },
    email: { 
      type: "mail",
    },
    birthday: { 
      type: "date", 
    },
    address: { 
      type: "date", 
    },
    idposition: { 
      type: "integer",
      minLength: 1 
    }
  },
  additionalProperties: false,
};
export default schema

