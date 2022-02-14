var schema = {
  type: "object",
  properties: {
    password_now: {
        type: "string",
        minLength: 8,
        maxLength: 15,
    },
    password_new: { 
        type: "string", 
        minLength: 8, 
        maxLength: 15 },
    re_password_new: { 
        type: "string", 
        minLength: 8, 
        maxLength: 15 },
  },
  additionalProperties: false,
};
export default schema
